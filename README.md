# NL_Enchants

**Neverland vanilla-friendly custom enchantments** for MythicEnchants +
MythicMobs. A production enchantment pack for the **Neverland Survival**
server: contextual effects, short reactive mechanics, readable VFX — every
enchantment explainable in one sentence.

- **Namespace:** `nl` (e.g. `nl:double_jump`)
- **Languages:** English (`en_us`) and Italian (`it_it`)
- **License:** MIT
- **Catalog:** 30 enchantments across 8 categories

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
4. Verify in-game: `/enchant @s nl:double_jump 1` on a pair of boots.

Full instructions and troubleshooting: [SETUP.md](SETUP.md).

## Folder structure

```text
NL_Enchants/
├── packinfo.yml                  MythicMobs pack metadata
├── enchantments/
│   └── <category>/<id>.yml       ONE FILE PER ENCHANTMENT (file name = ID)
├── skills/
│   └── <category>/<id>.yml       gameplay logic metaskills (NL_ENCHANT_*)
├── vfx/
│   └── <category>/<id>.yml       presentation metaskills (NL_VFX_*)
├── datapack/nl/                  namespace-scoped datapack fragments (tags)
├── resourcepack/                 client assets: en_us / it_it language entries
├── docs/
│   ├── enchantments/<id>.md      one specification per enchantment
│   ├── development.md · balancing.md · compatibility.md · localization.md
├── tools/validate.py             static validation (YAML, IDs, references, langs)
└── README.md · SETUP.md · CHANGELOG.md · LICENSE
```

## Enchantment catalog

Each entry links to a full specification in
[`docs/enchantments/`](docs/enchantments/) (effect, triggers, VFX, balance
notes, performance assessment, known limitations). Item groups: weapon =
swords+axes, armor = any piece, boots, bow, pickaxe, hoe, tools.

### Combat · `enchantments/combat/`

| ID | English | Italian | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- |
| `nl:sluggish` | Sluggish | Sbavato | UNCOMMON | III | weapon | Strikes can bog the target down in a viscous haze. |
| `nl:bleeding` | Bleeding | Sanguinante | UNCOMMON | III | weapon | Strikes can open wounds that keep hurting. |
| `nl:staggering` | Staggering | Barcollante | RARE | II | weapon | Strikes can briefly knock the target off balance. |
| `nl:executioner` | Executioner | Esecutore | RARE | III | weapon | Strikes against weakened targets hit harder — and you can see when. |
| `nl:predator` | Predator | Predatore | RARE | II | weapon | Strike back harder at the enemy that just hit you. |
| `nl:momentum` | Momentum | Impeto | UNCOMMON | III | weapon | Chained kills keep you fast — taking a hit breaks the flow. |
| `nl:echo` | Echo | Eco | EPIC | III | weapon | A part of your strike sometimes repeats a moment later. |
| `nl:mark` | Mark | Marchio | RARE | I | weapon | Your first hit marks a target; keeping the pressure rewarded. |

### Ranged · `enchantments/ranged/`

| ID | English | Italian | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- |
| `nl:hawkeye` | Hawkeye | Occhio di Falco | RARE | II | bow | Aim while standing still to empower your next fully-drawn shot. |
| `nl:ricochet` | Ricochet | Rimbalzo | EPIC | I | bow | A missed arrow springs once toward a nearby enemy. |
| `nl:recall` | Recall | Richiamo | UNCOMMON | I | bow | Arrows sometimes return to your quiver after landing. |

### Movement · `enchantments/movement/`

| ID | English | Italian | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- |
| `nl:double_jump` | Double Jump | Doppio Salto | RARE | I | boots | Press the jump key again while airborne to leap a second time. |
| `nl:shadowstep` | Shadowstep | Passo d'Ombra | RARE | I | boots | When struck, slip backward leaving a shadow of yourself behind. |
| `nl:climber` | Climber | Scalatore | UNCOMMON | I | boots | Sprint to climb ladders and vines faster; jump to leap off them. |

### Mining · `enchantments/mining/`

| ID | English | Italian | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- |
| `nl:shatter` | Shatter | Frantuma | RARE | III | pickaxe | Your picks sometimes crack the neighboring blocks of the same family. |
| `nl:prospector` | Prospector | Prospezione | RARE | I | pickaxe | Mining an ore pings when more treasure hides nearby. |
| `nl:conservation` | Conservation | Conservazione | UNCOMMON | II | tools | Your tools sometimes ignore wear. |

### Farming · `enchantments/farming/`

| ID | English | Italian | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- |
| `nl:green_thumb` | Green Thumb | Mano Verde | COMMON | II | hoe | Working the soil with your hoe sometimes encourages the crop. |
| `nl:reaping` | Reaping | Mietitura | RARE | I | hoe | Harvesting sometimes sweeps the neighboring crops in one go. |
| `nl:replanter` | Replanter | Ripiantatore | COMMON | I | hoe | Harvested crops are immediately replanted. |

### Defensive · `enchantments/defensive/`

| ID | English | Italian | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- |
| `nl:grounded` | Grounded | Radicamento | UNCOMMON | II | armor | You stand firm — a share of knockback slides off you. |
| `nl:reprisal` | Reprisal | Riflesso | UNCOMMON | III | armor | Blows against you sometimes bite back at the attacker. |
| `nl:second_wind` | Second Wind | Secondo Fiato | RARE | II | armor | At the brink, a burst of vigor carries you a little longer. |
| `nl:tenacity` | Tenacity | Tenacia | RARE | II | armor | Weathering blow after blow hardens you against the next ones. |

### Exploration · `enchantments/exploration/`

| ID | English | Italian | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- |
| `nl:sentinel` | Sentinel | Sentinella | RARE | I | helmet | Your helm quietly stirs when hostile eyes watch you. |
| `nl:wayfarer` | Wayfarer | Viandante | UNCOMMON | I | armor | Long stretches of honest travel reward you with a moment of vigor. |

### Legendary · `enchantments/legendary/`

| ID | English | Italian | Rarity | Max | Items | One-sentence effect |
| --- | --- | --- | --- | --- | --- | --- |
| `nl:resonance` | Resonance | Risonanza | LEGENDARY | I | armor | Attuned pieces hum together, slowly knitting your wounds. |
| `nl:voidbound` | Voidbound | Vincolato al Vuoto | MYTHIC | I | armor | Once, when death should have taken you, the void refuses to collect. |
| `nl:reflection` | Reflection | Riflesso Speculare | LEGENDARY | I | armor | Airborne steel turns against its archer. |
| `nl:soulbond` | Soulbond | Anima Gemella | LEGENDARY | I | armor | Bonded gear refuses to leave you — and binds its companions too. |

> **Naming note:** the original concept list assigned the Italian name
> *Riflesso* to both Reprisal and Reflection. Reprisal keeps *Riflesso*
> (as specified first); Reflection uses *Riflesso Speculare* — IDs are
> unaffected. See `docs/enchantments/reflection.md`.

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

> **Validation status:** *Static validation completed (30 enchants, 0
> errors). Runtime validation on Paper + MythicMobs + MythicEnchants is
> still required* — including the per-enchant RUNTIME-VERIFY items flagged
> in `docs/enchantments/*.md` and `docs/compatibility.md`. Nothing in this
> repository should be considered in-game tested until verified on the live
> server.

## Troubleshooting

| Symptom | Likely cause / fix |
| --- | --- |
| Enchantments don't appear after install | You restarted only once — restart again (datapack two-phase load) |
| Parse warnings about enchantment files on a server without MythicEnchants | Expected files are skipped via `FileDependencies`; install MythicEnchants |
| Movement enchants stop working after relogging | MythicMobs drops auras on quit — re-equip the boots |
| Enchantment names not translated in-game | Resource pack not merged, or the datapack bakes server-side strings — see `docs/localization.md` |
| `/enchant nl:...` unknown | Pack folder not directly under `plugins/MythicMobs/packs/NL_Enchants/` |

## Contributing

1. Follow the syntax policy — no invented mechanics; every non-obvious line
   cites its official documentation page.
2. One enchantment per change set, specification first, validator green.
3. Keep IDs, commits and changelog entries consistent with
   `docs/development.md`.
