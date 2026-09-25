# Reprisal

```text
ID:                nl:reprisal
Italian name:      Riflesso
English name:      Reprisal
Category:          defensive
Rarity:            UNCOMMON
Maximum Level:     3
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         nl:reflection
Trigger(s):        ~onDamaged → metaskill @trigger
Cooldown:          1s internal
```

## Effect

20% chance to bite back at the attacker for 1/2/3 damage (level, thorns cause).

## VFX

Damage-indicator pulse + thorns chime.

## Balance

Vanilla-thorns flavored. Conflicts with reflection.

## Notes

Identity: RETALIATION.

## Files

```text
enchantments/defensive/reprisal.yml
skills/defensive/reprisal.yml            (when the logic lives in metaskills)
vfx/defensive/reprisal.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
