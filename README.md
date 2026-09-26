# NL_Enchants

**English** · [Italiano](README.it.md)

**Neverland vanilla-friendly custom enchantments** for MythicEnchants +
MythicMobs. A production enchantment pack for the **Neverland Survival**
server: contextual effects, short reactive mechanics, readable VFX — every
enchantment explainable in one sentence.

- **Namespace:** `nl` (e.g. `nl:swift_strike`)
- **Languages:** English (`en_us`) and Italian (`it_it`)
- **License:** MIT
- **Catalog:** 14 enchants across 5 categories
- **Status:** v0.6.0 — vanilla+ utility set (owner list); MythicStats-based passives; runtime testing pending

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
4. Verify in-game: `/enchant @s nl:swift_strike 1` on a sword.

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

14 enchants, ported from the server-owner vanilla+ utility list (mechanics-verified — see `docs/catalog-plan.md`; 4 skips with reasons in `docs/enchantments/_skipped-from-list.md`).

> Tooltips: vanilla shows only the name — the description line needs the client mod "Enchantment Descriptions" (see SETUP.md). This table is the reference.

### Combat

| Enchantment | ID | Max | Rarity | What it does |
| --- | --- | --- | --- | --- |
| Ice Aspect | `nl:ice_aspect` | 2 | RARE | 10%/lvl: freezes the victim solid for 3s (they can still look around and fight) |
| Websnare | `nl:websnare` | 2 | UNCOMMON | 8+8%/lvl: a cobweb spawns under the victim, trapping them |
| Swift Strike | `nl:swift_strike` | 5 | UNCOMMON | +0.6 attack speed/lvl — up to 75% faster attack recovery at L5 |
| Outreach | `nl:outreach` | 2 | RARE | +0.5/lvl attack reach — up to 4 blocks at L2 |

### Bows

| Enchantment | ID | Max | Rarity | What it does |
| --- | --- | --- | --- | --- |
| Toxic | `nl:toxic` | 1 | UNCOMMON | arrows poison the victim 11s; undead are immune. Bow only |
| Breeze Burst | `nl:breeze_burst` | 1 | RARE | arrows burst with wind on impact and drop a Wind Charge |

### Tools

| Enchantment | ID | Max | Rarity | What it does |
| --- | --- | --- | --- | --- |
| Crab's Touch | `nl:crabs_touch` | 3 | RARE | +1/lvl block reach (7.5 at L3); works held in the offhand too — reach blocks AND place from afar |

### Defense

| Enchantment | ID | Max | Rarity | What it does |
| --- | --- | --- | --- | --- |
| Vitality | `nl:vitality` | 3 | RARE | +2 max health/lvl — 13 hearts at L3 while worn |
| Skyguard | `nl:skyguard` | 4 | RARE | elytra only: −4%/lvl damage taken (Protection for elytras) |
| Kinetic Protection | `nl:kinetic_protection` | 4 | UNCOMMON | −25%/lvl elytra kinetic damage (crash into walls) |
| Retrieval | `nl:retrieval` | 4 | UNCOMMON | 20%/lvl: arrows that hit you are retrieved into your inventory (80% at L4) |
| Graviole | `nl:graviole` | 3 | RARE | elytra only: gravity −10%/lvl — longer, floatier flights, slower top speed |

### Movement

| Enchantment | ID | Max | Rarity | What it does |
| --- | --- | --- | --- | --- |
| Scorch Walker | `nl:scorch_walker` | 2 | RARE | walk on lava on magma blocks; immune to magma and powder snow; L2 also to lava |
| Stride | `nl:stride` | 3 | UNCOMMON | step up full blocks without jumping (higher steps at L2/L3) |

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
