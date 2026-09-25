# Executioner

```text
ID:                nl:executioner
Italian name:      Esecutore
English name:      Executioner
Category:          combat
Rarity:            RARE
Maximum Level:     3
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onAttack → metaskills @target
Cooldown:          marker line 3s internal
```

## Effect

Below 30% health, attacks deal +1/+2/+3 bonus damage (level). A 3s-gated marker shows the target is vulnerable.

## VFX

Angry-villager symbol above the target; crit burst on the strike.

## Balance

Finisher identity; the telegraph is part of the design.

## Notes

Identity: FINISHER.

## Files

```text
enchantments/combat/executioner.yml
skills/combat/executioner.yml            (when the logic lives in metaskills)
vfx/combat/executioner.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
