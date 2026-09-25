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
Trigger(s):        ~onDamaged @trigger + ~onAttack @target
Cooldown:          —
```

## Effect

When hit, the attacker is stalked for 5s. Hitting the stalker deals +1/+2 (level) bonus damage and consumes the stalk.

## VFX

Soul particles burst + wolf growl on the counter-strike.

## Balance

Counterplay against a SPECIFIC attacker (aura on the attacker entity). One charge per window.

## Notes

Identity: REACTION / COUNTERPLAY.

## Files

```text
enchantments/combat/predator.yml
skills/combat/predator.yml            (when the logic lives in metaskills)
vfx/combat/predator.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
