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
Trigger(s):        ~onDamaged
Cooldown:          5s internal
```

## Effect

When struck, 25% chance to slip backward (relative -Z hop, +0.1 Y) leaving a shadow afterimage.

## VFX

Smoke + soul silhouette at the old position, muffled enderman teleport sound.

## Balance

Evasive, not offensive: fixed small hop, 5s cooldown. No speed effect by design (see master spec).

## Notes

Identity: MOVEMENT VISUAL / MOBILITY. Upgrade path (ItemDisplay afterimage) documented in repo docs; needs verified summon/despawn first.

## Files

```text
enchantments/movement/shadowstep.yml
skills/movement/shadowstep.yml
vfx/movement/shadowstep.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
