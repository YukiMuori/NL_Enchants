# Echo

```text
ID:                nl:echo
Italian name:      Eco
English name:      Echo
Category:          combat
Rarity:            EPIC
Maximum Level:     3
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onAttack
Cooldown:          2s internal
```

## Effect

25% of hits repeat after 0.3s, dealing 10%/20%/30% (by level) of the original attack's damage (item_attack based).

## VFX

End-rod burst + evoker whisper at the delayed second impact — clearly distinguishable from the swing.

## Balance

item_attack scales with the weapon, so the echo never outgrows the weapon itself. 2s internal cooldown prevents machine-gun spam.

## Notes

Identity: DELAYED HIT.

## Files

```text
enchantments/combat/echo.yml
skills/combat/echo.yml
vfx/combat/echo.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
