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
Trigger(s):        ~onAttack → metaskill @target
Cooldown:          —
```

## Effect

On hit: 5/10/15% chance (level × 5%) to apply Slowness I for 2.5s.

## VFX

Falling-honey drips + honey place sound on the target.

## Balance

Control proc, conflicts with staggering. Flat Slowness I (never stacked amplifiers).

## Notes

Identity: CONTROL.

## Files

```text
enchantments/combat/sluggish.yml
skills/combat/sluggish.yml            (when the logic lives in metaskills)
vfx/combat/sluggish.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
