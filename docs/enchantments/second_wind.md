# Second Wind

```text
ID:                nl:second_wind
Italian name:      Secondo Fiato
English name:      Second Wind
Category:          defensive
Rarity:            RARE
Maximum Level:     2
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         nl:voidbound
Trigger(s):        ~onDamaged → metaskill @self
Cooldown:          45s internal
```

## Effect

When a hit drops you below 30% health: Regeneration I + Speed I for 3s. (v0.3.0: fixed durations — constants only.)

## VFX

Heart particles + brewing fizz.

## Balance

45s cooldown; regen-only healing.

## Notes

Identity: EMERGENCY RESPONSE.

## Files

```text
enchantments/defensive/second_wind.yml
skills/defensive/second_wind.yml            (when the logic lives in metaskills)
vfx/defensive/second_wind.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
