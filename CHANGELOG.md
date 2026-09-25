# Changelog

All notable changes to NL_Enchants are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/) · Versioning:
[SemVer](https://semver.org/) — MAJOR breaking · MINOR enchant/feature ·
PATCH fix/balance. Gameplay values are never changed silently.

## [0.1.0] — 2026-09-25

Initial public scaffold of the pack: repository architecture, pack
metadata, localization layer, and the reference implementation enchantment.

### Added

- **Repository structure & metadata**: `packinfo.yml` (MythicMobs pack
  metadata, `FileDependencies` on MythicEnchants), `SETUP.md`, `README.md`,
  `LICENSE` (MIT), `.gitignore`, `datapack/nl/` namespace placeholder,
  layered `enchantments/ · skills/ · vfx/` architecture per category.
- **Enchantment `nl:double_jump` ("Double Jump" / "Doppio Salto")** —
  movement, RARE, MaxLevel I, boots (`#minecraft:enchantable/foot_armor`).
  After jumping, pressing the jump key again while airborne performs a
  second, vanilla-strength leap; driven by a 5-second self-expiring charge
  granted on every ground jump. Full specification:
  `docs/enchantments/double_jump.md`.
- **Skills**: `skills/movement/double_jump.yml` — equip/unequip listener
  auras (Paper `onJump` + `OnInput` components), charge arming, guarded
  second-jump impulse.
- **VFX**: `vfx/movement/double_jump_vfx.yml` — activation-only cloud/end-rod
  burst + layered airy audio (22 particles, 2 sounds per activation).
- **Localization**: `resourcepack/` with `en_us` and `it_it` enchantment
  name + description entries and `pack.mcmeta`; localization policy in
  `docs/localization.md`.
- **Documentation**: `docs/development.md` (architecture, conventions,
  verified-syntax policy, checklist), `docs/balancing.md`,
  `docs/compatibility.md` (Paper-only features, Geyser caveat, edge cases).
- **Tooling**: `tools/validate.py` — static validation of YAML, enchant ID
  namespace/rules, required fields, skill-ID uniqueness, `skill{s=}`
  reference resolution, localization completeness, per-enchant docs.

### Validation status

- Static validation: **completed** (see `tools/validate.py`).
- Runtime validation on Paper + MythicMobs + MythicEnchants:
  **required** — not yet performed.

[0.1.0]: https://github.com/YukiMuori/NL_Enchants/releases/tag/v0.1.0
