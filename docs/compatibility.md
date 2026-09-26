# Compatibility

## Target platform

| Component | Requirement | Notes |
| --- | --- | --- |
| Server | **Paper** 1.21.11+ (or compatible forks) | Hard requirement of MythicEnchants; also required by this pack (see below) |
| Java | 25 | MythicEnchants requirement |
| Minecraft | 1.21.11+ | datapack-driven enchantments |
| MythicMobs | 5.12.0+ | free version works; no premium features are used |
| MythicEnchants | current | provides the enchantment registration + `nl:` datapack namespace |

Per MythicEnchants setup docs: first install needs **two server restarts**,
and adding/removing enchantments always requires a full restart (datapack
registration). Skill/VFX edits can be applied with `/mm reload` /
`/mench reload`.

## Paper-only features used by this pack

- `onJump` aura mechanic — MythicMobs, Paper-only.
- `OnInput` aura component — MythicMobs, Paper-only.

Spigot-only servers are **not** supported by this pack. This matches the
platform MythicEnchants already requires.

## Not supported

- **Geyser / Bedrock clients** — MythicEnchants custom enchantments do not
  work over Geyser (upstream limitation); no workaround is planned.
- **MythicCrucible / ModelEngine** — not required. The pack deliberately
  uses only vanilla particles/sounds and documented MythicMobs mechanics so
  there is no optional dependency to manage. If a future signature VFX
  genuinely needs a custom model, it will be introduced as an explicit,
  documented optional dependency (`FileDependencies`) — never silently.

## Known runtime edge cases (to verify in-game)

The authoritative test protocol is `docs/testing.md`. Architecture-level
checks that gate several enchants:

- **Listener-aura enchants** (`nl:ninja`, `nl:haste`, `nl:replenish`,
  `nl:waterborne`) after a **relog**: MythicMobs
  cleans auras on quit; re-equipping restores them unless MythicEnchants
  re-fires `~onEquip` at login (verify and update the specs accordingly).
- **`<skill.var.enchant-level>` inside metaskills**: any console error
  naming the variable invalidates rule R1 — report immediately.
- **`~onBlockBreak` gates** (`triggerblocktype` with vanilla block tags):
  confirm tag form behaves like the documented tag/material form.
- **`<skill.var.enchant-level>` arithmetic inside metaskills** (e.g.
  `<skill.var.enchant-level+1>`): if console errors name the variable,
  fall back to per-level constants and report.
- **`recoveritem` re-equip** (`nl:soulbond`): confirm `reequip=true`
  restores armor to the correct slot after death recovery.
- **`nl:grounded` set stacking**: 4× II pieces reach 80% knockback
  resistance — verify feel in PvP.
- **`nl:ricochet`** spawned meta-projectile: confirm visuals, damage and
  protection-plugin compatibility (EXPERIMENTAL flag in spec).

## Datapack & resource pack interplay

- MythicEnchants auto-generates the live datapack in each world. This pack
  never writes into the world folder.
- `resourcepack/` only contains language entries and must be merged into (or
  shipped alongside) the server's client resource pack — see `SETUP.md` and
  `docs/localization.md`.
