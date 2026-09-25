# Shadowstep

```text
ID:                nl:shadowstep
Italian name:      Passo d'Ombra
English name:      Shadowstep
Category:          movement
Rarity:            RARE
Maximum Level:     1
Supported Items:   #minecraft:enchantable/foot_armor
Valid Slots:       FEET
Conflicts:         none
Trigger(s):        ~onDamaged → metaskill @self
Cooldown:          5s internal
```

## Effect

When struck, 25% chance to slip backward (relative -Z hop) leaving a shadow afterimage.

## VFX

Smoke + soul silhouette, muffled enderman teleport sound.

## Balance

Evasive, not offensive; 5s cooldown.

## Notes

Identity: MOVEMENT VISUAL / MOBILITY.

## Files

```text
enchantments/movement/shadowstep.yml
skills/movement/shadowstep.yml            (when the logic lives in metaskills)
vfx/movement/shadowstep.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
