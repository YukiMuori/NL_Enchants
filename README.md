# NL_Enchants

**English** · [Italiano](README.it.md)

**Neverland vanilla-friendly custom enchantments** for MythicEnchants +
MythicMobs. A production enchantment pack for the **Neverland Survival**
server: contextual effects, short reactive mechanics, readable VFX — every
enchantment explainable in one sentence.

- **Namespace:** `nl` (e.g. `nl:thor`)
- **Languages:** English (`en_us`) and Italian (`it_it`)
- **License:** MIT
- **Catalog:** 38 enchants across 6 categories
- **Status:** v0.5.0 — Vanilla+ catalog (ported from the AdvancedEnchantments Vanilla+ list); runtime testing on server pending

## Requirements

| Component | Version |
| --- | --- |
| Paper server | 1.21.11+ |
| Java | 25 |
| MythicMobs | 5.12.0+ |
| MythicEnchants | current release |

> MythicEnchants itself requires Paper — so does this pack (several of its
> runtime hooks are Paper-only MythicMobs features). No other plugins are
> required; no premium features are used.

## Installation

1. Copy this repository (or a release archive) into
   `plugins/MythicMobs/packs/NL_Enchants/`.
2. Restart the server **twice** (first start deploys the datapack, second
   start registers the enchantments — a MythicEnchants data-driven
   requirement).
3. Merge the `resourcepack/` folder into your server resource pack
   (language entries only — see `SETUP.md`).
4. Verify in-game: `/enchant @s nl:thor 1` on a sword.

Full instructions and troubleshooting: [SETUP.md](SETUP.md).

## Folder structure

```text
NL_Enchants/
├── packinfo.yml                  MythicMobs pack metadata
├── enchantments/
│   └── <category>/<id>.yml       ONE FILE PER ENCHANTMENT (file name = ID)
├── skills/
│   └── <category>/<id>.yml       gameplay logic metaskills (NL_ENCHANT_*)
├── skills/vfx/                   presentation metaskills (NL_VFX_*)
├── datapack/nl/                  namespace-scoped datapack fragments (tags)
├── resourcepack/                 client assets: en_us / it_it language entries
├── docs/
│   ├── enchantments/<id>.md      one specification per enchantment
│   ├── development.md · balancing.md · compatibility.md · localization.md
├── tools/validate.py             static validation (YAML, IDs, references, langs)
└── README.md · SETUP.md · CHANGELOG.md · LICENSE
```

## Enchantment catalog

38 enchants across 6 categories, ported from the AdvancedEnchantments "Vanilla+" list.
Per-enchant design notes live in `docs/enchantments/<id>.md`; what was skipped and why is in `docs/enchantments/_skipped-from-ae-list.md`.
### Combat

| Enchantment | ID | Max | Rarity |
| --- | --- | --- | --- |
| Arctic Freeze | `nl:arctic_freeze` | 3 | UNCOMMON |
| Blackout | `nl:blackout` | 5 | UNCOMMON |
| Double Blow | `nl:double_blow` | 4 | RARE |
| Drain | `nl:drain` | 7 | RARE |
| Enderbane | `nl:enderbane` | 5 | RARE |
| Zombie Crusher | `nl:zombie_crusher` | 3 | UNCOMMON |
| Skullcrusher | `nl:skullcrusher` | 3 | UNCOMMON |
| Incinerate | `nl:incinerate` | 3 | UNCOMMON |
| Blaze Reaper | `nl:blaze_reaper` | 3 | RARE |
| Cubism | `nl:cubism` | 3 | UNCOMMON |
| First Strike | `nl:first_strike` | 3 | UNCOMMON |
| Finishing | `nl:finishing` | 3 | UNCOMMON |
| Postpone | `nl:postpone` | 3 | COMMON |
| Repel | `nl:repel` | 3 | COMMON |
| Starvation | `nl:starvation` | 3 | COMMON |
| Thor | `nl:thor` | 3 | RARE |
| Ninja | `nl:ninja` | 3 | RARE |
| Ravenous | `nl:ravenous` | 4 | UNCOMMON |### Ranged

| Enchantment | ID | Max | Rarity |
| --- | --- | --- | --- |
| Multi-Shot | `nl:multi_shot` | 3 | RARE |
| Flashbang | `nl:flashbang` | 3 | UNCOMMON |
| Frost | `nl:frost` | 3 | UNCOMMON |
| Explosive | `nl:explosive` | 5 | RARE |### Mining

| Enchantment | ID | Max | Rarity |
| --- | --- | --- | --- |
| Blast Mining | `nl:blast_mining` | 3 | RARE |
| Experience | `nl:experience` | 5 | UNCOMMON |
| Foraging | `nl:foraging` | 3 | COMMON |
| Nether Prospector | `nl:nether_prospector` | 3 | UNCOMMON |
| Haste | `nl:haste` | 3 | RARE |### Defensive

| Enchantment | ID | Max | Rarity |
| --- | --- | --- | --- |
| Adrenaline | `nl:adrenaline` | 3 | UNCOMMON |
| End Affinity | `nl:end_affinity` | 3 | UNCOMMON |
| Nether Affinity | `nl:nether_affinity` | 3 | UNCOMMON |
| Rebounding | `nl:rebounding` | 3 | RARE |
| Rumble | `nl:rumble` | 3 | UNCOMMON |
| Scorching | `nl:scorching` | 3 | COMMON |
| Vanish | `nl:vanish` | 3 | UNCOMMON |
| Waterborne | `nl:waterborne` | 1 | UNCOMMON |### Movement

| Enchantment | ID | Max | Rarity |
| --- | --- | --- | --- |
| Escape | `nl:escape` | 2 | COMMON |
| Feather Step | `nl:feather_step` | 5 | RARE |### Farming

| Enchantment | ID | Max | Rarity |
| --- | --- | --- | --- |
| Replenish | `nl:replenish` | 1 | COMMON |
## Rarity

Rarity describes an enchantment's identity and grouping; enchanting-table
availability is controlled separately by each enchantment's `Enchanting`
weight and cost range (MythicEnchants decouples the two by design).

```text
COMMON (5) · UNCOMMON (9) · RARE (12) · EPIC (2) · LEGENDARY (3) · MYTHIC (1)
```

Rarity distribution follows a pyramid: simple utility sits low, signature
mechanics sit at LEGENDARY/MYTHIC.

## Languages

All enchantment names and descriptions are provided in English and Italian
(`resourcepack/assets/minecraft/lang/`). Internal IDs are
language-independent and never change. See
[docs/localization.md](docs/localization.md).

## Reloading

- **Adding or removing an enchantment** → full server restart (datapack
  registration; `/mm reload` is not enough).
- **Changing skills/VFX of an existing enchantment** → `/mm reload` (or
  `/mench reload`) is sufficient.

## Development workflow

See [docs/development.md](docs/development.md) for the layered architecture,
the verified-syntax policy, the new-enchantment checklist and the commit
conventions. Static validation:

```bash
python3 tools/validate.py
```

> **Validation status:** *v0.3.0 is a reliability rebuild — static
> validation completed; runtime validation on Paper + MythicMobs +
> MythicEnchants is REQUIRED.* Follow `docs/testing.md` (per-enchant test
> matrix) and report console errors. Nothing is considered working until it
> passes that protocol.

## Troubleshooting

| Symptom | Likely cause / fix |
| --- | --- |
| Enchantments don't appear after install | You restarted only once — restart again (datapack two-phase load) |
| Parse warnings about enchantment files on a server without MythicEnchants | Expected files are skipped via `FileDependencies`; install MythicEnchants |
| Movement enchants stop working after relogging | MythicMobs drops auras on quit — re-equip the boots |
| Enchantment names not translated in-game | Resource pack not merged, or the datapack bakes server-side strings — see `docs/localization.md` |
| `/enchant nl:...` unknown | Pack folder not directly under `plugins/MythicMobs/packs/NL_Enchants/` |
| Some enchantments deal no damage / no VFX after `/mm reload` | Console says `Could not find MetaSkill NL_VFX_...` → you kept the old `vfx/` folder: VFX now live under `skills/vfx/` (rule R9) |
| Mining/farming enchants missing from `/enchant` | Console datapack error about `SupportedItems` tags → use v0.3.2+ (`enchantable/mining` + PrimaryItems) |

## Contributing

1. Follow the syntax policy — no invented mechanics; every non-obvious line
   cites its official documentation page.
2. One enchantment per change set, specification first, validator green.
3. Keep IDs, commits and changelog entries consistent with
   `docs/development.md`.
