# Reflection

```text
ID:                nl:reflection
Italian name:      Riflesso Speculare
English name:      Reflection
Category:          legendary
Rarity:            LEGENDARY
Maximum Level:     1
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         nl:reprisal
Trigger(s):        ~onDamaged ?lastdamagecause{c=PROJECTILE}
Cooldown:          8s internal
```

## Effect

Projectile hits are halved (reducedamage cap=0.5); the shooter takes a fixed 4 damage back.

## VFX

End-rod shimmer + glassy shatter.

## Balance

Controlled partial reflect, projectiles only.

## Notes

Identity: DEFENSIVE REACTION.

## Files

```text
enchantments/legendary/reflection.yml
skills/legendary/reflection.yml            (when the logic lives in metaskills)
vfx/legendary/reflection.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
