# Ricochet

```text
ID:                nl:ricochet
Italian name:      Rimbalzo
English name:      Ricochet
Category:          ranged
Rarity:            EPIC
Maximum Level:     1
Supported Items:   #minecraft:enchantable/bow
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onShoot + ~onBowMiss
Cooldown:          one bounce per 4s window
```

## Effect

Within 4s of a shot, a missed arrow springs once toward the nearest hostile within 10 blocks, dealing 4 damage.

## VFX

End-rod trail on the spring projectile; spark + arrow-hit sound on the bounce.

## Balance

One ricochet per shot window (aura consumed). Flat damage (not bow-scaled) keeps it from stacking with Power. If no hostile is near, the charge is wasted.

## Notes

Identity: PROJECTILE BEHAVIOR.

## Files

```text
enchantments/ranged/ricochet.yml
skills/ranged/ricochet.yml
vfx/ranged/ricochet.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
