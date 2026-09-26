# In-Game Testing Protocol

**Static validation ≠ runtime validation.** This is the checklist for
runtime verification on Paper + MythicMobs + MythicEnchants. Nothing is
"done" until it passes here.

## Before you start

1. Install the pack (`SETUP.md`), restart **twice**.
2. Enable whatever debug the plugins expose (`/mm debug` if available) and
   keep the **console open** — failed skill lines print errors there. When
   an enchant "does nothing", the console almost always says why.
3. Grant yourself test items with `/enchant @s <id> <level>`.

Report back, for each enchant: WORKS / FAILS + the exact console error
lines (if any) + one sentence about the feel (too strong/weak/often).

## Per-enchant test matrix

| Enchant | Test | Expected |
| --- | --- | --- |
| `nl:double_jump` | Wear boots, jump, press jump again mid-air (also try holding) | second vanilla-strength leap + puff |
| `nl:shadowstep` | Wear boots, take a melee hit several times | occasional backward slip + smoke |
| `nl:climber` | Wear boots, hold sprint on a ladder/vine; press jump on it | faster climb; jump-off leap |
| `nl:sluggish` III | Hit a mob ~20 times | ~1 slow proc every 2–3 hits, 2.5s Slowness I |
| `nl:bleeding` III | Hit a mob ~20 times | occasional 1-damage ticks ×4 + end burst |
| `nl:staggering` II | Hit a mob ~20 times | occasional brief stutter-pin |
| `nl:executioner` III | Damage a mob below 30%, then hit | marker symbol sometimes; hits deal +3 |
| `nl:predator` II | Let a mob hit you, then hit it back | +2 on the first counter-hit only |
| `nl:momentum` | Kill 3 mobs in a row without taking damage | Speed I each kill; breaks on damage |
| `nl:echo` III | Hit mobs ~20 times | occasional second impact after ~0.3s |
| `nl:mark` | Hit one mob twice | first hit marks (glow), second hits +1.5 |
| `nl:hawkeye` II | Shoot fully drawn vs quick-release | full draw: +1.5 arrow dmg + burst |
| `nl:ricochet` | Miss a shot near a hostile within 8 blocks | arrow sprite springs once, 4 dmg |
| `nl:recall` | Shoot ~30 arrows | ~1 in 3 misses returns an arrow |
| `nl:shatter` III | Mine stone/ores repeatedly | occasional neighbor crack (≤12/≤8) |
| `nl:prospector` | Mine ore near/beside hidden diamonds | strong chime vs soft tick |
| `nl:conservation` II | Mine a lot; watch durability | noticeably slower wear |
| `nl:green_thumb` II | Harvest crops repeatedly | occasional growth burst around you |
| `nl:reaping` | Harvest wheat with neighbors | 35% sweep of the 3×3 |
| `nl:replanter` | Harvest crops | instant replant every time |
| `nl:grounded` II×4 | Wear full set; take knockback (explosions) | strongly reduced knockback |
| `nl:reprisal` III | Get hit repeatedly | ~1 in 5 hits reflects 3 dmg |
| `nl:second_wind` | Drop below 30% HP once, then again within 45s | once: regen+speed burst; then: nothing for 45s |
| `nl:tenacity` | Take hits every <5s for a while | Resistance I during the chain |
| `nl:sentinel` | Stand near hostiles | glow pulse + chime every 5s |
| `nl:wayfarer` | Sprint outdoors for a minute | regen pulse every ~60s while moving |
| `nl:resonance` | Get hit wearing 1 piece, then the full set | Regen I 3s vs Regen II 8s (20s cd each); no load errors from resonance.yml |
| `nl:voidbound` | Take a killing blow (twice, 10 min apart) | survive at ~0 HP + Absorption; second time nothing |
| `nl:reflection` | Get shot repeatedly | ~half damage taken + shooter bites back, 8s gate |
| `nl:soulbond` | Die wearing a piece (3 times) | item kept + re-equipped each time, 3rd death it drops |

## Architecture-level checks (these gate several enchants)

- **A1 — `~onEquip` on login**: equip listener enchants, relog → do the
  listeners still fire? If not, re-equip restores them (documented).
- **A2 — aura tick targeting**: bleeding/heartbeat enchants tick on the
  right entity (bleeding damages the victim, not the attacker).
- **A3 — `<skill.var.enchant-level>` in metaskills**: any console error
  mentioning the variable means the form is wrong — report immediately.
- **A4 — enchant variables in aura ticks**: expected NOT to work; the pack
  must not produce errors for them (constants only by design).

## Field-log fixes already applied (0.3.0 → 0.3.2)

- `hasMythicEnchant` in skill files failed to load → moved to enchant
  lines (R8); console must show NO "Failed to load custom condition".
- All `NL_VFX_*` were missing → packs only load conventional folders;
  VFX moved under `skills/vfx/` (R9). After reload the console must NOT
  contain any "Could not find MetaSkill NL_VFX_" line.
- `#minecraft:enchantable/pickaxe|hoe` rejected → 5 enchants were skipped
  from the datapack; now `enchantable/mining` + PrimaryItems (R10).
  Console must show NO "[Datapack] ... Skipped" lines.
- `triggerblocktype` tag gates never matched → material lists now.

## Known-risk list (from the rebuild)

- `~onUse`-dependent designs were REMOVED (hawkeye, green_thumb redesigned).
- `nl:ricochet` uses a spawned meta-projectile — EXPERIMENTAL flag in spec.
- Listener-aura enchants (double_jump, climber, sentinel, wayfarer,
  resonance) depend on A1.
