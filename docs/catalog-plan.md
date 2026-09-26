# Catalog plan — v0.6.0 "Vanilla+ utility" set

Source: 18-enchants list provided by the server owner (vanilla+ datapack
style: Breeze Burst … Websnare). Method per R6: every enchant was mapped
onto mechanics verified on the official MythicMobs / MythicEnchants docs
(see docs/development.md). 14 ship; 4 are documented skips
(`_skipped-from-list.md`). Nothing was invented to close a gap.

## New capability unlocked this round: MythicStats

The MythicEnchants "MythicStats" field (official ME wiki docs) applies
MythicMobs built-in stats while the item is equipped. The built-in stat
list includes vanilla attributes, which directly power six of the
requested enchants:

| Enchant | Stat | Scaling |
| --- | --- | --- |
| Crab's Touch | BLOCK_INTERACTION_RANGE | +1.0/lvl (→ 7.5 reach) |
| Outreach | ENTITY_INTERACTION_RANGE | +0.5/lvl (→ 4.0 reach) |
| Swift Strike | ATTACK_SPEED | +0.6/lvl |
| Stride | STEP_HEIGHT | +0.45/lvl |
| Vitality | HEALTH | +2.0/lvl (→ 13 hearts) |
| Graviole | GRAVITY | −0.1/lvl |

The validator now accepts a MythicStats-only enchant (no Skills block).

## Shipped (14)

| Category | Enchants |
| --- | --- |
| combat | `nl:ice_aspect` (2) · `nl:websnare` (2) · `nl:swift_strike` (5) · `nl:outreach` (2) |
| ranged | `nl:toxic` (1) · `nl:breeze_burst` (1) |
| mining | `nl:crabs_touch` (3) |
| defensive | `nl:vitality` (3) · `nl:skyguard` (4) · `nl:kinetic_protection` (4) · `nl:retrieval` (4) · `nl:graviole` (3) |
| movement | `nl:stride` (3) · `nl:scorch_walker` (2) |

## Documented adaptations

- **Breeze Burst** — fires on entity impact (no projectile-block-impact
  trigger exists in ME); grants both the wind burst and a collectible
  Wind Charge item.
- **Retrieval** — the arrow that hit still drops; the enchant adds a
  retrieved arrow (plain) on chance. Tipped effects not replicated.
- **Scorch Walker** — one magma block under the feet (no frost-walker
  surface generation); L2 adds lava-damage immunity.
- **Toxic** — bow only (bow+crossbow would need two SupportedItems tags,
  illegal per R11).
- **Outreach / Swift Strike** — scoped to `#minecraft:enchantable/sharp_weapon`
  (no sword-only tag exists); spec's sword-only table scope noted.
- **Ice Aspect / Outreach / Swift Strike** — spec-listed incompatibilities
  are documented only: ME has no verified incompatibility option.
- **Elytra enchants** (Graviole, Skyguard) — elytra lives in
  `#minecraft:enchantable/equippable`, narrowed with PrimaryItems.

## "Found in…" loot placement — out of scope (documented)

The source list specifies loot sources (trial-chamber vaults, end-city
chests, librarian trades…). MythicEnchants has no verified loot-table
integration; placement is a server-owner task using vanilla loot tables —
the `nl:` IDs work in vanilla `set_enchantments` loot functions.
