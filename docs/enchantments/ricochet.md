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
Trigger(s):        ~onShoot (arm) + ~onBowMiss
Cooldown:          one spring per 4s window
```

## Effect

Within 4s of a shot, a missed arrow springs once toward the nearest hostile within 8 blocks, dealing 4 damage. EXPERIMENTAL: spawned meta-projectile — verify feel in-game.

## VFX

End-rod trail; spark + arrow-hit sound on the bounce.

## Balance

One charge per shot window (aura consumed). Flat damage.

## Notes

Identity: PROJECTILE BEHAVIOR.

## Files

```text
enchantments/ranged/ricochet.yml
skills/ranged/ricochet.yml            (when the logic lives in metaskills)
vfx/ranged/ricochet.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
