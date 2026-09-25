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

Projectile hits are halved; the removed half is dealt back to the shooter.

## VFX

End-rod shimmer + glassy shatter tinkle.

## Balance

Controlled partial reflect (50%) gated to projectiles only — not a generic 'return 50% damage'. Italian display name is 'Riflesso Speculare' (documented deviation: reprisal owns 'Riflesso').

## Notes

Identity: DEFENSIVE REACTION.

## Files

```text
enchantments/legendary/reflection.yml
skills/legendary/reflection.yml
vfx/legendary/reflection.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
