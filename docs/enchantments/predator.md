# Predator

```text
ID:                nl:predator
Italian name:      Predatore
English name:      Predator
Category:          combat
Rarity:            RARE
Maximum Level:     2
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onDamaged + ~onAttack
Cooldown:          —
```

## Effect

When hit, the attacker is stalked for 5s. Hitting the stalker deals +2/+3 bonus damage and consumes the stalk.

## VFX

Soul particles burst + wolf growl on the counter-strike.

## Balance

Reaction/counterplay vs a SPECIFIC attacker (aura tag on the attacker entity), not a generic multiplier. One charge per window.

## Notes

Identity: REACTION / COUNTERPLAY.

## Files

```text
enchantments/combat/predator.yml
skills/combat/predator.yml
vfx/combat/predator.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
