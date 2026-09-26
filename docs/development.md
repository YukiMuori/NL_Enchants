# Development Guide

This document describes how NL_Enchants is structured and how to add a new
enchantment without breaking the pack.

## Layered architecture

Every enchantment is split into three layers. Gameplay logic and presentation
must never be mixed inside one skill.

```text
enchantments/<category>/<id>.yml  the enchantment definition — THIN dispatcher,
                                  ONE FILE PER ENCHANT (file name = enchant ID)
skills/<category>/<id>.yml        gameplay logic (NL_ENCHANT_* metaskills)
skills/vfx/<category>/<id>.yml    presentation only (NL_VFX_* metaskills)
                                  (must be under skills/ — see rule R9)
resourcepack/                     client-side names/descriptions (en_us, it_it)
docs/enchantments/<id>.md         the human-readable specification
```

The enchantment's `Skills:` section only dispatches to metaskills:

```yaml
nl:example:
  Skills:
  - skill{s=NL_ENCHANT_EXAMPLE_SOMETHING} @self ~onTrigger
```

Small self-contained behaviors (e.g. replanter's four `setblock` lines, or
`conservation`'s single `unbreaking` line) may live inline in the
enchantment file when a metaskill would add nothing. VFX always live in
`vfx/`.

Reference implementations: `nl:double_jump` (listener-aura architecture) and
`nl:executioner` (direct trigger lines). Copy their structure.

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
| `~onBlockBreak` trigger + `veinminer` origin semantics | MythicEnchants → VeinMiner |
| `~onItem_damage` trigger (unbreaking usage) | MythicEnchants → Unbreaking |
| `~onUse` (bow draw), `~onBowMiss`, `arrowbuff`, `projectilepath` | MythicEnchants → ProjectilePath / ArrowBuff, MM Triggers |
| `recoveritem` on `~onDeath` | MythicEnchants → RecoverItem (official example) |
| `reducedamage` (flat, cause filter, cap) with `<math:damage>` | MythicEnchants → ReduceDamage (official examples) |
| `lethalcheck` inline on `~onDamaged` | MythicEnchants → LethalCheck (official example) |
| `hasMythicEnchant` (id/level/slot), `itemDurability`, `batchedchance` | MythicEnchants → Conditions |
| `addcounter` / `?counter` / `<counter.KEY>` | MythicEnchants → Counter |
| Rarity tiers incl. `RARE`, `LEGENDARY`, `MYTHIC` | MythicEnchants → Rarities |
| Valid `#minecraft:enchantable/*` tags (armor, foot_armor, ..., weapon, melee_weapon, sharp_weapon, bow, mining, durability, ... — NO pickaxe/hoe) | MythicEnchants datapack validator error, field log 0.3.1 |
| `triggerblocktype` accepts material lists, rejects `#` block tags | MythicEnchants TriggerBlockTypeFilter warning, field log 0.3.1 |
| MythicMobs packs load conventional folders only (Skills/, Items/, ...) | MythicMobs Packs page + field log 0.3.1 |
| `onJump` aura mechanic (Paper-only) | MythicMobs → Mechanics → onjump |
| `OnInput` aura component (`requirejump`, `requiresprint`) | MythicMobs → Aura Components → OnInput |
| `OnBlockBreak` component (`oB=`, `bt=`) + recursion warning | MythicMobs → Aura Components → OnBlockBreak |
| `aura` (stacks, refresh, CancelOnTakeDamage, ot/oe), `auraremove`, `hasaura` | MythicMobs → Aura / Conditions |
| `velocity` (SET/ADD, relative), `potion` (type/d/l/hasParticles) | MythicMobs → Mechanics |
| `damage{a=...;cause=...}`, `setblock{m=...}`, `dropitem{i=...}`, `bonemeal`, `particles`, `sound` | MythicMobs → Mechanics |
| `projectile{v;mr;d;gravity;fromorigin;oT;oH}` + `@EntitiesInRadius{r;limit;sort;targetPlayers}` | MythicMobs → Projectile / Targeters (official examples) |
| `@TargetBlock{maxdistance}`, `@MobsInRadius`, `@BlocksInRadius`, `@origin`, `@trigger`, `@self`, `@targetlocation` | MythicMobs → Targeters / official examples |
| `bowtension{value=>0.9}`, `healthpercent{p=<30%}`, `lastdamagecause{c=...}`, `mobsinradius{types;a;r}`, `blocktype{type=...}`, `blocktypeinradius{t;a;r}`, `triggerblocktype{t=...}`, `onground`, `outside`, `moving`, `isclimbing`, `chance{c=...}` | MythicMobs → Conditions (+ ME quick-start for `chance`) |
| Composite inline conditions `?((a && b) || (c d))` + condition actions (`false`, `castinstead`) | MythicMobs → Inline Conditions / Conditions |
| `<math:EXPR>` with `enchant_level`, `damage`, `item_attack` variables | MythicEnchants → Enchantment Config |
| Paper jump event is ground-only (no mid-air press event) | Paper PlayerJumpEvent javadoc |

Deliberately NOT used (kept out of the free-feature set): Premium-only
inline targeter conditions, `onBounceSkill` (Premium), ModelEngine,
MythicCrucible.

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

## Reliability rules (v0.3.0 — learned from the 0.2.0 field failure)

The 0.2.0 catalog largely failed in-game. Root cause analysis and the rules
now enforced for every line of this pack:

- **R1 — Variable forms are context-dependent.** `<skill.var.enchant-level>`
  is the documented form inside metaskills (MythicEnchants injects it into
  the skill tree). The bare `<math:enchant_level>` form is documented only
  in the enchantment's DIRECT skill lines. 0.2.0 used the bare form inside
  metaskills → unresolvable → the line errored → the whole metaskill
  aborted. Rule: metaskills use `<skill.var.enchant-level>`; direct lines
  may use `<math:...>`; **aura tick/delayed skills use constants only**
  (variables are not guaranteed to survive into later execution contexts).
- **R2 — Dispatch lines mirror official examples.** `~onAttack → @target`,
  `~onDamaged → @self` (wearer effects) or `@trigger` (attacker effects),
  `~onBlockBreak → @self` (veinminer semantics) or `@origin` (setblock),
  `~onShoot → @self`.
- **R3 — Metaskill mechanics inherit.** Mechanics without a targeter
  inherit the dispatch targeter (documented Metaskills behavior). Explicit
  `@target`/`@self` only where an override is intended.
- **R4 — One condition per line; lists only where proven.** Comma lists
  inside `triggerblocktype` ARE required and work (generic condition-array
  behavior; '#' block tags are REJECTED there — field-verified 0.3.1
  "unrecognized material — it will never match"). Lists are otherwise only
  allowed inside mechanics that document them (veinminer skips unknown
  entries by design).
- **R5 — `CancelIfNoTargets: false`** on utility metaskills that are not
  guaranteed a target (default is `true`, which silently cancels).
- **R6 — Only documented mechanics.** Every mechanic/condition/targeter
  must exist on its own wiki page or in an official example. Anything else
  is marked EXPERIMENTAL in the spec and testing docs.
- **R7 — Prefer boring.** A simpler enchant that always works beats a
  clever one that sometimes works.
- **R9 — Pack folders are conventional.** MythicMobs packs load known
  folders (Skills/, Items/, Mobs/, ...). A custom root `vfx/` folder is
  silently IGNORED (field-verified 0.3.1: every NL_VFX_* metaskill was
  "Could not find MetaSkill"). All metaskills therefore live under
  `skills/` — VFX in `skills/vfx/<category>/`. The validator errors if a
  root `vfx/` folder reappears.
- **R10 — SupportedItems uses only real tags.** The MythicEnchants
  datapack validator rejects unknown `#minecraft:enchantable/*` tags and
  SKIPS the enchantment from the datapack (field-verified 0.3.1:
  pickaxe/hoe tags do not exist). Valid tags are whitelisted in the
  validator; narrow scoping is done with PrimaryItems material keys.
- **R8 — MythicEnchants conditions only in enchantment files.**
  `hasMythicEnchant` (and friends) FAIL TO LOAD inside plain MythicMobs
  skill files (field-verified 0.3.0: "Failed to load custom condition").
  Use them in the enchantment's direct `Skills:` lines as inline
  conditions (`?mench{...}`), one condition per line. The validator
  enforces this. Cross-slot logic must therefore be event-time, on the
  enchant line, with a graceful fallback if the gate ever fails.

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
