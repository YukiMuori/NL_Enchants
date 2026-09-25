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
Trigger(s):        ~onAttack → metaskill @target
Cooldown:          2s internal
```

## Effect

25% of hits repeat after 0.3s dealing +1/+2/+3 damage (level). (v0.3.0: flat level-scaled instead of item_attack — the attack-damage variable is not guaranteed inside metaskills.)

## VFX

End-rod burst + evoker whisper at the delayed impact.

## Balance

Fixed value = predictable and readable. 2s internal cooldown.

## Notes

Identity: DELAYED HIT.

## Files

```text
enchantments/combat/echo.yml
skills/combat/echo.yml            (when the logic lives in metaskills)
vfx/combat/echo.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
