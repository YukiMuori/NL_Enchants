# Green Thumb

```text
ID:                nl:green_thumb
Italian name:      Mano Verde
English name:      Green Thumb
Category:          farming
Rarity:            COMMON
Maximum Level:     2
Supported Items:   #minecraft:enchantable/hoe
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onUse (hoe use)
Cooldown:          —
```

## Effect

Using the hoe looking at a crop: 15/20% chance to apply a free bone-meal growth tick to it.

## VFX

Composter sparkles + bone-meal sound at the crop.

## Balance

Modest free growth — single block, crop-only (blocktype gate), modest chance.

## Notes

Identity: FARMING. RUNTIME-VERIFY: ~onUse on hoe + @TargetBlock behavior.

## Files

```text
enchantments/farming/green_thumb.yml
skills/farming/green_thumb.yml
vfx/farming/green_thumb.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
