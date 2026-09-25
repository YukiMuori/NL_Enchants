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
Trigger(s):        ~onBlockBreak on crops (4 gate lines)
Cooldown:          —
```

## Effect

Harvesting a crop: 5/10% chance (level × 5%) for a burst of growth — bonemeal applied to the blocks around you. REDESIGNED v0.3.0: the hoe-~onUse design relied on unverified behavior.

## VFX

Composter sparkles + bone-meal sound.

## Balance

Bonemeal on grass can pop flowers — a fitting vanilla flourish.

## Notes

Identity: FARMING.

## Files

```text
enchantments/farming/green_thumb.yml
skills/farming/green_thumb.yml            (when the logic lives in metaskills)
vfx/farming/green_thumb.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
