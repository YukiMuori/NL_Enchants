# Reaping

```text
ID:                nl:reaping
Italian name:      Mietitura
English name:      Reaping
Category:          farming
Rarity:            RARE
Maximum Level:     1
Supported Items:   #minecraft:enchantable/hoe
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onBlockBreak on crops (4 gate lines)
Cooldown:          veinminer throttle perblock=2
```

## Effect

35% chance to also break matching crops in the 3×3×3 (max 8).

## VFX

Wheat-chip particles + grass break sound.

## Balance

Immature neighbors may break (seeds only) — documented; pairs with replanter.

## Notes

Identity: AREA HARVESTING.

## Files

```text
enchantments/farming/reaping.yml
skills/farming/reaping.yml            (when the logic lives in metaskills)
vfx/farming/reaping.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
