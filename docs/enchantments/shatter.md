# Earthshatter (nl:shatter)

```text
ID:                nl:shatter  (ID kept for item compatibility)
Italian name:      Spaccaterra
English name:      Earthshatter
Category:          mining
Rarity:            RARE
Maximum Level:     3
Supported Items:   #minecraft:enchantable/mining (Primary: pickaxes)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onBlockBreak (material-list gates)
Cooldown:          veinminer throttle (perblock=2)
```

## Effect

5/10/15% chance (stone family, level×5%) or 4/8/12% (ores, level×4%) for
the pick to send cracks through the neighboring same-family blocks — a
3×3×3 shockwave (max 12 stone / 8 ore). Drops use the held tool (Fortune /
Silk Touch respected); per-block durability applies.

## VFX

Core `NL_VFX_EARTH_SHOCKWAVE`: cobble crack spray, crit dust, wide end-rod
ring, deep explosion + deepslate boom.

## Balance / Safety

veinminer publishes synthetic BlockBreakEvents per block, so protection
plugins (claims, regions) can veto each break — the safe area-mining
design. Built-in re-entrancy guard prevents recursion; maxblocks caps
worst case.

## Files

```text
enchantments/mining/shatter.yml
skills/mining/shatter.yml
skills/core/ring.yml
```
