# Staggering

```text
ID:                nl:staggering
Italian name:      Barcollante
English name:      Staggering
Category:          combat
Rarity:            RARE
Maximum Level:     2
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         nl:sluggish
Trigger(s):        ~onAttack → metaskill @target
Cooldown:          —
```

## Effect

On hit: 5/10% chance (level × 5%) to lift the target slightly and pin it in place for ~0.3s.

## VFX

Crit particle burst + iron golem impact sound.

## Balance

Physical interruption — no slow, no damage. Conflicts with sluggish.

## Notes

Identity: INTERRUPTION / PHYSICAL CONTROL.

## Files

```text
enchantments/combat/staggering.yml
skills/combat/staggering.yml            (when the logic lives in metaskills)
vfx/combat/staggering.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
