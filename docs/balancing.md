# Balancing

Values are in the enchant files only — never changed silently; changes
require a version bump and a CHANGELOG entry.

## Rarity bands

| Rarity | Weight | MinCost | MaxCost | Anvil |
| --- | --- | --- | --- | --- |
| COMMON | 6 | 4 | 24 | 1 |
| UNCOMMON | 5 | 8 | 30 | 2 |
| RARE | 3 | 16 | 38 | 4 |

## Per-enchant values (v0.6.0)

| Enchant | Levels | Core numbers |
| --- | --- | --- |
| `nl:swift_strike` | 5 | +0.6/lvl attack speed (base 4.0 → +3.0 at L5) |
| `nl:stride` | 3 | +0.45/lvl step height (0.6 → 1.05/1.5/1.95) |
| `nl:vitality` | 3 | +2/lvl max health (+6 = 13 hearts at L3) |
| `nl:outreach` | 2 | +0.5/lvl entity reach (3.0 → 3.5/4.0) |
| `nl:crabs_touch` | 3 | +1.0/lvl block reach (4.5 → 5.5/6.5/7.5); main+offhand |
| `nl:graviole` | 3 | gravity −10%/lvl on elytra |
| `nl:ice_aspect` | 2 | 10%/lvl; freeze 3s |
| `nl:websnare` | 2 | 8+8%/lvl; cobweb persists |
| `nl:toxic` | 1 | poison 11s; undead immune; bow only |
| `nl:breeze_burst` | 1 | wind burst + 1 Wind Charge item on arrow entity-impact |
| `nl:kinetic_protection` | 4 | −25%/lvl kinetic damage (FLY_INTO_WALL) |
| `nl:skyguard` | 4 | −4%/lvl all damage on elytra |
| `nl:retrieval` | 4 | 20%/lvl (→ 80%); plain arrows |
| `nl:scorch_walker` | 2 | magma under feet in lava; negate HOT_FLOOR+FREEZE; L2 + LAVA |

## Tuning notes

- MythicStats values are ADDITIVE over vanilla bases (reach 4.5/3.0,
  attack speed 4.0, step height 0.6, health 20, gravity 1.0).
- Stat-based passives have no proc RNG — balance via magnitude per level.
- Graviole's trade (longer flight vs slower top speed) is inherent to
  lowering gravity: the dive is what builds elytra speed.
- Cobwebs (Websnare) persist; consider a cleanup policy if players abuse
  terrain clutter — current decision: vanilla behavior, no cleanup.
