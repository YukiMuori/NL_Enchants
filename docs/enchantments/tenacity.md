# Tenacity

```text
ID:                nl:tenacity
Italian name:      Tenacia
English name:      Tenacity
Category:          defensive
Rarity:            RARE
Maximum Level:     2
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         none
Trigger(s):        ~onDamaged → metaskills @self
Cooldown:          1s internal
```

## Effect

First hit in a window starts a 5s hardened state; further hits while hardened grant Resistance I for 3s and refresh it. (v0.3.0: fixed values.)

## VFX

End-rod pulse + faint bell ring.

## Balance

Rewards tanking sustained fights; nothing vs burst.

## Notes

Identity: SUSTAINED DEFENSE.

## Files

```text
enchantments/defensive/tenacity.yml
skills/defensive/tenacity.yml            (when the logic lives in metaskills)
vfx/defensive/tenacity.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
