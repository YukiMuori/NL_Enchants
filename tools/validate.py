#!/usr/bin/env python3
"""NL_Enchants static validator.

Static checks only — a green run does NOT mean the pack was runtime-tested.
Runtime validation on Paper + MythicMobs + MythicEnchants is still required.

Checks
  1. All YAML files parse (packinfo.yml, enchantments/, skills/, vfx/).
  2. Enchant IDs are namespaced `nl:<lowercase_snake_case>` and unique.
  3. Required enchant fields: Display, MaxLevel, ValidSlots, SupportedItems, Skills.
  4. Skill IDs unique across skills/ and vfx/; NL_ prefix convention.
  5. Every `skill{s=...}` / `skill{skill=...}` reference resolves.
  6. Every aura removed via `auraremove{aura=X}` is applied via `auraname=X`.
  7. Every enchant has en_us + it_it lang entries (name and `.desc`).
  8. Every production enchant has a docs/enchantments/<id>.md spec file.
  9. packinfo.yml has Name/Version/Author.

Usage:  python3 tools/validate.py   (repo root; requires PyYAML)
"""

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required:  pip install pyyaml")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent

ENCHANT_ID_RE = re.compile(r"^nl:[a-z][a-z0-9_]*$")
SKILL_REF_RE = re.compile(r"skill\{[^}]*?\bs(?:kill)?\s*=\s*([A-Za-z0-9_]+)")
AURANAME_RE = re.compile(r"auraname\s*=\s*([A-Za-z0-9_]+)")
AURAREMOVE_RE = re.compile(r"auraremove\{[^}]*?aura\s*=\s*([A-Za-z0-9_]+)")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_yaml(path: Path):
    try:
        with path.open("r", encoding="utf-8") as fh:
            return yaml.safe_load(fh)
    except yaml.YAMLError as exc:
        err(f"YAML parse error in {path.relative_to(ROOT)}: {exc}")
        return None


def main() -> int:
    # ── 1+2+3: enchantments ────────────────────────────────────────────────
    enchants: dict[str, Path] = {}
    skill_texts: list[tuple[Path, str]] = []

    for path in sorted((ROOT / "enchantments").rglob("*.yml")):
        data = load_yaml(path)
        if not isinstance(data, dict):
            err(f"{path.relative_to(ROOT)}: top level must be a mapping of enchant IDs")
            continue
        for eid, cfg in data.items():
            label = f"{path.relative_to(ROOT)}:{eid}"
            if not ENCHANT_ID_RE.match(str(eid)):
                err(f"{label}: enchant ID must match nl:<lowercase_snake_case>")
                continue
            if eid in enchants:
                err(f"{label}: duplicate enchant ID (also in {enchants[eid].relative_to(ROOT)})")
                continue
            enchants[eid] = path
            if not isinstance(cfg, dict):
                err(f"{label}: enchant config must be a mapping")
                continue
            for field in ("Display", "MaxLevel", "ValidSlots", "SupportedItems", "Skills"):
                if field not in cfg:
                    err(f"{label}: missing required field '{field}'")
            skills = cfg.get("Skills")
            if isinstance(skills, list):
                for line in skills:
                    skill_texts.append((path, str(line)))

    # ── 4: skill / vfx definitions ─────────────────────────────────────────
    defined_skills: dict[str, Path] = {}
    for section in ("skills", "vfx"):
        base = ROOT / section
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.yml")):
            data = load_yaml(path)
            if not isinstance(data, dict):
                err(f"{path.relative_to(ROOT)}: top level must be a mapping of skill IDs")
                continue
            for sid, cfg in data.items():
                sid = str(sid)
                if sid in defined_skills:
                    err(f"{path.relative_to(ROOT)}:{sid}: duplicate skill ID "
                        f"(also in {defined_skills[sid].relative_to(ROOT)})")
                    continue
                defined_skills[sid] = path
                if not sid.startswith("NL_"):
                    warn(f"{path.relative_to(ROOT)}:{sid}: skill ID lacks the NL_ prefix")
                if isinstance(cfg, dict):
                    for line in cfg.get("Skills") or []:
                        skill_texts.append((path, str(line)))
                    for line in cfg.get("Conditions") or []:
                        skill_texts.append((path, str(line)))

    # ── 5: skill references ────────────────────────────────────────────────
    for path, line in skill_texts:
        for ref in SKILL_REF_RE.findall(line):
            if ref not in defined_skills:
                err(f"{path.relative_to(ROOT)}: reference to undefined skill '{ref}'")

    # ── 6: aura cleanup ────────────────────────────────────────────────────
    applied: set[str] = set()
    removed: set[str] = set()
    for path in list((ROOT / "skills").rglob("*.yml")) + list((ROOT / "vfx").rglob("*.yml")) + \
                list((ROOT / "enchantments").rglob("*.yml")):
        text = path.read_text(encoding="utf-8")
        applied |= set(AURANAME_RE.findall(text))
        removed |= set(AURAREMOVE_RE.findall(text))
    for name in sorted(removed - applied):
        err(f"aura '{name}' removed via auraremove but never applied (auraname=...)")

    # ── 7: localization ────────────────────────────────────────────────────
    lang_dir = ROOT / "resourcepack" / "assets" / "minecraft" / "lang"
    langs: dict[str, dict] = {}
    for code in ("en_us", "it_it"):
        f = lang_dir / f"{code}.json"
        if not f.is_file():
            err(f"missing resource pack language file: {f.relative_to(ROOT)}")
            continue
        try:
            langs[code] = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            err(f"{f.relative_to(ROOT)}: invalid JSON: {exc}")
    for eid in enchants:
        key_base = "enchantment." + eid.replace(":", ".")  # nl:double_jump → enchantment.nl.double_jump
        for key in (key_base, f"{key_base}.desc"):
            for code, table in langs.items():
                if key not in table:
                    err(f"{code}.json: missing translation key '{key}'")

    # ── 8: per-enchant documentation ───────────────────────────────────────
    for eid, path in enchants.items():
        doc = ROOT / "docs" / "enchantments" / f"{eid.split(':', 1)[1]}.md"
        if not doc.is_file():
            err(f"{path.relative_to(ROOT)}:{eid}: missing spec file {doc.relative_to(ROOT)}")

    # ── 9: packinfo ────────────────────────────────────────────────────────
    info = load_yaml(ROOT / "packinfo.yml")
    if isinstance(info, dict):
        for field in ("Name", "Version", "Author"):
            if field not in info:
                err(f"packinfo.yml: missing field '{field}'")
    elif info is not None:
        err("packinfo.yml: top level must be a mapping")

    # ── report ─────────────────────────────────────────────────────────────
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(enchants)} enchant(s), {len(defined_skills)} skill/vfx definition(s), "
          f"{len(warnings)} warning(s), {len(errors)} error(s)")
    if errors:
        print("STATIC VALIDATION FAILED")
        return 1
    print("STATIC VALIDATION PASSED — runtime validation on "
          "Paper + MythicMobs + MythicEnchants is still required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
