# In-Game Testing Protocol

**Static validation ≠ runtime validation.** This is the checklist for
runtime verification on Paper + MythicMobs + MythicEnchants. Nothing is
"done" until it passes here.

## Before you start

1. Install the pack (`SETUP.md`), restart **twice** (delete
   `world/datapacks/MythicEnchants/` if upgrading over an older build).
2. Keep the **console open** — failed skill lines print errors there.
3. Grant test items with `/enchant @s <id> <level>`.

Report back, for each enchant: WORKS / FAILS + the exact console error
lines (if any) + one sentence about the feel (too strong/weak/often).

## Architecture gates (check these FIRST — they gate 6 enchants)

- **MythicStats system**: watch the console on startup for MythicStats /
  unknown-mechanic errors. Gate for Swift Strike, Stride, Vitality,
  Outreach, Crab's Touch, Graviole. If absent → update MythicMobs.
- **Negative stat amount** (`nl:graviole`, GRAVITY −0.1/lvl): verify the
  <math:> expression resolves (console names the line if not).
- **Elytra scoping**: `/enchant @s nl:skyguard 1` + `/enchant @s
  nl:graviole 1` on an ELYTRA (not a chestplate) — equippable tag +
  PrimaryItems.
- **`FLY_INTO_WALL` cause** (`nl:kinetic_protection`): if it never
  triggers, the cause name is wrong on this server — quote the console.

## Per-enchant test matrix

| Enchant | Test | Expected |
| --- | --- | --- |
| `nl:swift_strike` | L1 vs L5, swing repeatedly | cooldown clearly shorter; L5 near-spam |
| `nl:stride` | walk into a 1-block step (L1), slab+wall (L2/L3) | steps up without jumping |
| `nl:vitality` | wear L1→L3, check hearts; unequip | 22/24/26 max HP; restored on unequip; check after death |
| `nl:outreach` | L2, hit a mob at ~3.5–4 blocks | connects; vanilla 3.0 does not |
| `nl:crabs_touch` | L3, break/place at 6–7.5 blocks; tool in OFFHAND | reach works; offhand placing works |
| `nl:graviole` | fly with L1/L3 elytra | floatier glide, longer airtime, lower top speed |
| `nl:ice_aspect` | hit ~10× L1, ~10× L2 | frozen 3s ~10%/20%; frozen mobs still rotate/attack |
| `nl:websnare` | hit ~15× | cobweb under victim sometimes; cobweb breaks normally |
| `nl:toxic` | shoot zombie vs skeleton | poison 11s on zombie; skeleton unaffected |
| `nl:breeze_burst` | shoot mobs ~10× | wind pop + Wind Charge item drops at the victim |
| `nl:kinetic_protection` | elytra-crash into a wall at L1..L4 | 25/50/75/100% less kinetic damage |
| `nl:skyguard` | take hits L1 vs L4 | damage down 4%/16% |
| `nl:retrieval` | let a skeleton shoot you ~10× per level | arrows fly into inventory 20→80% |
| `nl:scorch_walker` | swim in lava L1; stand on magma / powder snow; L2 swim again | magma under feet, cross the lake; HOT_FLOOR+FREEZE negated; L2: lava damage negated; boots unequip stops it |

## Known documented deviations (not bugs)

- Breeze Burst fires on ENTITY impact, not block impact (no such trigger).
- Retrieval grants a plain arrow on top of the normal arrow drop.
- Scorch Walker generates one block under the feet, not a surface.
- Toxic is bow-only (R11).
- Spec incompatibilities (Ice Aspect/Websnare/Fire Aspect; Outreach/Swift
  Strike) are NOT enforced — ME has no verified incompatibility option.
