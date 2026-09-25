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
Trigger(s):        ~onBlockBreak
Cooldown:          veinminer throttle perblock=2
```

## Effect

Breaking stone-family or ore blocks: 15/20/25% (stone) or 12/16/20% (ores) chance to crack matching neighbors in a 3x3x3 (max 12 stone / 8 ore blocks). Drops use the held tool (Fortune/Silk Touch respected); durability is consumed per block.

## VFX

Crit crackle + sweep sound at the break.

## Balance

 veinminer's built-in re-entrancy guard prevents recursion; maxblocks caps worst case. No auto-chain beyond one cube.

## Notes

Identity: AREA MINING. Same-material-family scoping documented.

## Files

```text
enchantments/mining/shatter.yml
skills/mining/shatter.yml
vfx/mining/shatter.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
