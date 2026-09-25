# Shatter

```text
ID:                nl:shatter
Italian name:      Frantuma
English name:      Shatter
Category:          mining
Rarity:            RARE
Maximum Level:     3
Supported Items:   #minecraft:enchantable/pickaxe
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onBlockBreak (one gate line per vanilla block tag/material)
Cooldown:          veinminer throttle perblock=2
```

## Effect

5/10/15% (stone, level×5%) or 4/8/12% (ores, level×4%) chance to crack matching neighbors in a 3×3×3 (max 12 stone / 8 ore). Drops respect the held tool.

## VFX

Crit crackle + sweep sound at the broken block.

## Balance

veinminer's built-in re-entrancy guard prevents recursion; maxblocks caps worst case. Gates are single-tag conditions (verified form); material lists live only in veinminer's own filter (unknown entries skipped by design).

## Notes

Identity: AREA MINING.

## Files

```text
enchantments/mining/shatter.yml
skills/mining/shatter.yml            (when the logic lives in metaskills)
vfx/mining/shatter.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
