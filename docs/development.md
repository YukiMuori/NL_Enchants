# Development Guide

This document describes how NL_Enchants is structured and how to add a new
enchantment without breaking the pack.

## Layered architecture

Every enchantment is split into three layers. Gameplay logic and presentation
must never be mixed inside one skill.

```text
enchantments/<category>.yml      the enchantment definition — a THIN dispatcher
skills/<category>/<enchant>.yml  gameplay logic (NL_ENCHANT_* metaskills)
vfx/<category>/<enchant>_vfx.yml presentation only (NL_VFX_* metaskills)
resourcepack/                    client-side names/descriptions (en_us, it_it)
docs/enchantments/<enchant>.md   the human-readable specification
```

The enchantment's `Skills:` section only dispatches to metaskills:

```yaml
nl:example:
  Skills:
  - skill{s=NL_ENCHANT_EXAMPLE_SOMETHING} @self ~onTrigger
```

Reference implementation: `nl:double_jump` (see
`docs/enchantments/double_jump.md`). Copy its structure for new enchantments.

## Conventions

### Identifiers

- Enchantment IDs are **always** explicitly namespaced: `nl:<lowercase_snake_case>`.
  The namespace is frozen forever once an enchant is released — display names
  may change, IDs may not.
- Skill IDs: `NL_ENCHANT_<ENCHANT>_<PURPOSE>` (gameplay) and
  `NL_VFX_<ENCHANT>_<PURPOSE>` (presentation). Uppercase, grep-able, unique
  across the whole pack.
- Aura names used internally: `nl_<short_name>` (e.g. `nl_dj_charge`).
- File layout follows the Mythic Pack system:
  `plugins/MythicMobs/packs/NL_Enchants/<folder>/...`.

### Syntax policy

No syntax may be invented. Before using any mechanic, targeter, trigger,
condition or config field:

1. Verify it on the official wiki (wiki.mythiccraft.io — MythicMobs and
   MythicEnchants sections).
2. Then search this repository for prior usage.
3. Only then write it — with a comment linking the reference page when the
   usage is non-obvious.

Currently load-bearing verified facts (re-verify after plugin upgrades):

| Fact | Source |
| --- | --- |
| Enchant config fields (Display, MaxLevel, ValidSlots, SupportedItems, Enchanting, Options, Skills) | MythicEnchants → Enchantment Config |
| `~onEquip` / `~onUnequip` enchantment triggers | MythicEnchants → MythicStats page, Enchantment Config example |
| Rarity tiers incl. `RARE`, `LEGENDARY` | MythicEnchants → Rarities |
| `#minecraft:enchantable/foot_armor` item tag | Minecraft 1.21+ item tags |
| `onJump` aura mechanic (Paper-only) | MythicMobs → Mechanics → onjump |
| `OnInput` aura component, `requirejump` | MythicMobs → Aura Components → OnInput |
| `velocity`, `particles`, `sound`, `aura`, `auraremove`, `setvariable`, `delay`, `skill` mechanics | MythicMobs → Mechanics |
| `hasaura`, `onground`, `variableisset`, inline `?cond` / `?!cond` | MythicMobs → Conditions / Inline Conditions |
| Paper jump event is ground-only (no mid-air press event) | Paper PlayerJumpEvent javadoc |

## Adding a new enchantment — checklist

1. Inspect the catalog (`README.md`, `docs/enchantments/`) for mechanic
   duplication. Merge, redesign or reject overlaps — and document the decision.
2. Write the specification first (all fields from §28 of the design doc) in
   `docs/enchantments/<id>.md`.
3. Add the enchantment definition (`enchantments/<category>.yml`) as a thin
   dispatcher.
4. Implement gameplay skills (`skills/<category>/…`).
5. Implement VFX (`vfx/<category>/…`) — particles/sounds only.
6. Add both localizations (`resourcepack/assets/minecraft/lang/*.json`) and
   the `Display`/`Description` strings.
7. Update `README.md` (catalog table) and `CHANGELOG.md`.
8. Run `python3 tools/validate.py` — it must pass.
9. Review performance (see below) and note it in the enchant's doc file.
10. Commit with a conventional message (`feat: add <id> enchantment`).

## Performance rules

- Event-driven over polled: prefer triggers/aura components over timers.
- Any periodic check must be justified in the enchant's doc file.
- No permanent display entities; all spawned entities need guaranteed cleanup.
- VFX budgets: particle count and sound count are stated in every VFX file.
- No recursive skill chains without a hard depth or consumption guard.

## Validation

`tools/validate.py` performs static validation:

- YAML parses cleanly (all pack files + packinfo.yml)
- enchant IDs are `nl:`-namespaced, lowercase snake_case, unique
- required enchant fields present (Display, MaxLevel, ValidSlots,
  SupportedItems, Skills)
- skill IDs unique across `skills/` and `vfx/`
- every `skill{s=…}` reference resolves to a defined skill
- every enchant has `en_us` and `it_it` lang entries (name + `.desc`)
- every production enchant has a doc file in `docs/enchantments/`

```bash
python3 tools/validate.py
```

**Static validation ≠ runtime validation.** A passing validator never means
the pack was tested in-game. Runtime validation on Paper + MythicMobs +
MythicEnchants is still required — see `docs/compatibility.md`.

## Versioning & commits

- Semantic versioning: MAJOR breaking, MINOR new enchant/feature, PATCH
  fix/balance. Never change an enchant's gameplay silently.
- Conventional commit subjects: `feat:`, `fix:`, `balance:`, `docs:`,
  `refactor:`, `chore:`.
- Never commit server logs, world data, or generated artifacts.
