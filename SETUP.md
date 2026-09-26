# Setup

## 1. Server prerequisites

| Component | Version | Notes |
| --- | --- | --- |
| Paper | 1.21.11+ | forks compatible with Paper plugin API work |
| Java | 25 | required by MythicEnchants |
| MythicMobs | 5.12.0+ | free version is sufficient |
| MythicEnchants | current | installs as a MythicMobs add-on |

Install both plugins first and start the server once so MythicEnchants
creates its configuration.

## 2. Install the pack

Copy the repository contents so that the pack lives at:

```text
plugins/MythicMobs/packs/NL_Enchants/
├── packinfo.yml
├── enchantments/
├── skills/
├── skills/vfx/
├── datapack/
└── ...
```

The folder name `NL_Enchants` matters — keep it.

## 3. Restart twice

MythicEnchants registers enchantments through an auto-generated datapack:
the first restart deploys/regenerates it, the second one loads the newly
registered enchantments. Adding or removing enchantments in the future
always requires a full restart; editing skills/VFX of existing
enchantments only needs `/mm reload`.

If the datapack seems stale, `/mench refresh` regenerates it before the
next restart (per MythicEnchants docs).

## 4. Resource pack (languages + future assets)

`resourcepack/` contains `assets/minecraft/lang/en_us.json` and
`it_it.json` plus a `pack.mcmeta`. To ship it:

- **If you already run a server resource pack:** merge the `assets/` folder
  into your pack's `assets/` (paths do not overlap with vanilla assets) and
  keep your own `pack.mcmeta`.
- **If you do not run one:** zip the **contents** of `resourcepack/`
  (`pack.mcmeta` at the zip root) and host it; set
  `resource-pack=<url>` in `server.properties`.

Whether enchantment names resolve through these language files depends on
the datapack strings MythicEnchants generates — see
`docs/localization.md` for the verification procedure.

## 5. Verify

```text
/enchant @s nl:thor 1            → applies to held sword
```

Then hit a mob: occasional lightning strike. (`/mm reload` twice if the
first cast after a fresh install does nothing — see troubleshooting.)

### World names for the affinity enchants

`nl:end_affinity` and `nl:nether_affinity` gate on world names via the
MythicMobs `world` condition. The defaults cover the most common
Bukkit/Multiverse names; open
`enchantments/defensive/{end,nether}_affinity.yml` and edit the
`?world{w=...}` list to your server's actual world names if different.

## 6. Optional configuration (none required)

The pack requires **no changes** to your MythicEnchants or MythicMobs
global configuration. We intentionally do not distribute plugin config
files. If a future enchantment ever needs a non-default global setting,
this file will document the exact key, the value and the reason — you will
apply it manually.

## Troubleshooting

- **"Unknown enchantment" on `/enchant`** — pack folder not in
  `packs/NL_Enchants/`, or you haven't restarted twice, or the enchant ID
  was mistyped (IDs are `nl:<snake_case>`).
- **MythicMobs warnings about `enchantments/*.yml`** — MythicEnchants is
  missing; the pack declares `FileDependencies: enchantments/* MythicEnchants`
  so its enchantment files skip cleanly, but without MythicEnchants the pack
  does nothing.
- **Linux servers and folder casing** — MythicEnchants loads pack
  enchantments from `packs/<name>/enchantments/`; keep the lowercase folder
  names exactly as shipped in this repository.
- **First start errors about the datapack** — expected on a brand-new
  install; MythicEnchants regenerates and activates it on the second start.
- **Server refuses to boot with registry/datapack errors** (`Failed to
  load datapacks, can't proceed with server load`, or
  `Failed to parse nl:<id> from pack file`) — a generated datapack from a
  broken build is still in `world/datapacks/MythicEnchants/`. Update the
  pack folder, DELETE `world/datapacks/MythicEnchants/`, restart. If the
  error names an `nl:` enchant, report it — do not hand-edit the generated
  datapack (it is overwritten).
