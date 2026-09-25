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

- After a **relog**, MythicMobs auras are cleaned up; the double-jump
  listeners are restored by re-equipping the boots (unless MythicEnchants
  re-fires `~onEquip` at login — verify and update
  `docs/enchantments/double_jump.md` accordingly).
- A stale double-jump charge can survive a relog only for its remaining
  5-second window; it self-expires.

## Datapack & resource pack interplay

- MythicEnchants auto-generates the live datapack in each world. This pack
  never writes into the world folder.
- `resourcepack/` only contains language entries and must be merged into (or
  shipped alongside) the server's client resource pack — see `SETUP.md` and
  `docs/localization.md`.
