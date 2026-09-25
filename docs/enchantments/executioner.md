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
Trigger(s):        ~onAttack
Cooldown:          marker line 3s internal
```

## Effect

Below 30% health, attacks deal +1/+2/+3 bonus damage (by level). A 3s-gated marker (villager symbol + sound) shows when a target is vulnerable.

## VFX

Angry-villager symbol above the vulnerable target; crit burst + crit sound on the finishing strike.

## Balance

Finisher identity; the telegraph (marker) is part of the design so players learn the threshold.

## Notes

Identity: FINISHER.

## Files

```text
enchantments/combat/executioner.yml
skills/combat/executioner.yml
vfx/combat/executioner.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
