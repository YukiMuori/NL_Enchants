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
Trigger(s):        ~onBlockBreak
Cooldown:          veinminer throttle perblock=2
```

## Effect

35% chance when harvesting a crop to also break matching crops in the 3x3x3 around it (max 8).

## VFX

Wheat-chip particles + grass break sound at the harvested block.

## Balance

Documented compromise: immature neighbors break too (dropping only seeds) — crop-state checks are not available in the free syntax set; 35% keeps accidents rare. Pairs naturally with replanter.

## Notes

Identity: AREA HARVESTING.

## Files

```text
enchantments/farming/reaping.yml
skills/farming/reaping.yml
vfx/farming/reaping.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
