# NL_Enchants

**Neverland vanilla-friendly custom enchantments** for MythicEnchants +
MythicMobs. A production enchantment pack for the **Neverland Survival**
server: contextual effects, short reactive mechanics, readable VFX — every
enchantment explainable in one sentence.

- **Namespace:** `nl` (e.g. `nl:double_jump`)
- **Languages:** English (`en_us`) and Italian (`it_it`)
- **License:** MIT

## Requirements

| Component | Version |
| --- | --- |
| Paper server | 1.21.11+ |
| Java | 25 |
| MythicMobs | 5.12.0+ |
| MythicEnchants | current release |

> MythicEnchants itself requires Paper — so does this pack (two of its
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
4. Verify in-game: `/enchant @s nl:double_jump 1` on a pair of boots.

Full instructions and troubleshooting: [SETUP.md](SETUP.md).

## Folder structure

```text
NL_Enchants/
├── packinfo.yml              MythicMobs pack metadata
├── enchantments/             enchantment definitions (one file per category)
├── skills/                   gameplay logic metaskills (NL_ENCHANT_*)
├── vfx/                      presentation metaskills (NL_VFX_*)
├── datapack/nl/              namespace-scoped datapack fragments (tags)
├── resourcepack/             client assets: en_us / it_it language entries
├── docs/                     development, balancing, compatibility, localization
│   └── enchantments/         one specification per enchantment
├── tools/validate.py         static validation (YAML, IDs, references, langs)
├── README.md · SETUP.md · CHANGELOG.md · LICENSE
```

## Enchantment catalog

| ID | English | Italian | Category | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nl:double_jump` | Double Jump | Doppio Salto | movement | RARE | I | boots | After jumping, press the jump key again while airborne to leap a second time. |

> Planned categories: combat, ranged, movement, mining, farming, defensive,
> exploration, legendary. The pack grows incrementally — one fully specified,
> documented and runtime-verified enchantment at a time. Specifications for
> upcoming enchantments live in `docs/enchantments/`.

Each catalog entry links to a full specification in
[`docs/enchantments/`](docs/enchantments/) (effect, triggers, VFX, balance
notes, performance assessment, known limitations).

## Rarity

Rarity describes an enchantment's identity and grouping; enchanting-table
availability is controlled separately by each enchantment's `Enchanting`
weight and cost range (MythicEnchants decouples the two by design).

```text
COMMON · UNCOMMON · RARE · VERY_RARE · EPIC · LEGENDARY · MYTHIC
```

NL_Enchants reserves `LEGENDARY` and above for rare signature mechanics —
not every interesting enchant is legendary.

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

> **Validation status:** *Static validation completed.* *Runtime validation
> on Paper + MythicMobs + MythicEnchants is still required.* Nothing in this
> repository should be considered in-game tested until verified on the live
> server.

## Troubleshooting

| Symptom | Likely cause / fix |
| --- | --- |
| Enchantments don't appear after install | You restarted only once — restart again (datapack two-phase load) |
| Parse warnings about enchantment files on a server without MythicEnchants | Expected files are skipped via `FileDependencies`; install MythicEnchants |
| Double Jump stops working after relogging | MythicMobs drops auras on quit — take the boots off and put them back on |
| Enchantment names not translated in-game | Resource pack not merged, or the datapack bakes server-side strings — see `docs/localization.md` |
| `/enchant nl:...` unknown | Pack folder not directly under `plugins/MythicMobs/packs/NL_Enchants/` |

## Contributing

1. Follow the syntax policy — no invented mechanics; every non-obvious line
   cites its official documentation page.
2. One enchantment per change set, specification first, validator green.
3. Keep IDs, commits and changelog entries consistent with
   `docs/development.md`.
