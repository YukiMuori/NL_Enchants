# Sluggish

```text
ID:                nl:sluggish
Italian name:      Sbavato
English name:      Sluggish
Category:          combat
Rarity:            UNCOMMON
Maximum Level:     3
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         nl:staggering
Trigger(s):        ~onAttack
Cooldown:          —
```

## Effect

On hit: 12/16/20% chance (by level) to apply Slowness I for 2.5s (amplifier rises with level).

## VFX

Falling-honey drips + soft honey place sound on the target. 8 particles + 1 sound per proc.

## Balance

Control proc with explicit conflict vs staggering (only one control proc per weapon). Slowness never exceeds level I; duration fixed.

## Notes

Identity: CONTROL.

## Files

```text
enchantments/combat/sluggish.yml
skills/combat/sluggish.yml
vfx/combat/sluggish.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
