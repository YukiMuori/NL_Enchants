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

Per-enchant RUNTIME-VERIFY flags live in `docs/enchantments/*.md`. The
consolidated list:

- **Listener-aura enchants** (`nl:double_jump`, `nl:climber`) after a
  **relog**: MythicMobs cleans auras on quit; re-equipping the boots
  restores them unless MythicEnchants re-fires `~onEquip` at login (verify
  and update the specs accordingly).
- **`~onUse` draw behavior** (`nl:hawkeye`): frequency of firing while
  drawing, per the MythicEnchants projectilepath documentation.
- **`~onUse` on hoes** (`nl:green_thumb`): the `~onUse` trigger is
  documented for bow drawing; hoe usage needs in-game confirmation, with
  `@TargetBlock` resolving to the looked-at crop.
- **`@MobsInRadius{types=...}`** (`nl:sentinel`): confirm vanilla entity
  type names are accepted by the targeter's types filter, and review the
  hostile list against the server's custom mobs.
- **`triggerblocktype` with material lists** (`nl:shatter`, `nl:reaping`,
  `nl:replanter`): confirm comma lists behave like the documented single
  tag/material form.
- **`unbreaking{c=...}` on `~onItem_damage`** (`nl:conservation`): confirm
  the item-damage trigger also fires for tool-wear from block breaking.
- **`recoveritem` re-equip** (`nl:soulbond`): confirm `reequip=true` restores
  armor to the correct slot after death recovery.
- **`nl:grounded` set stacking**: 4× II pieces reach 80% knockback
  resistance — verify feel in PvP and retune if it reads as oppressive.
- **`projectile` spring** (`nl:ricochet`): confirm the spawned meta-projectile
  visuals/damage feel right and that `oH` damage honors protection plugins.

## Datapack & resource pack interplay

- MythicEnchants auto-generates the live datapack in each world. This pack
  never writes into the world folder.
- `resourcepack/` only contains language entries and must be merged into (or
  shipped alongside) the server's client resource pack — see `SETUP.md` and
  `docs/localization.md`.
