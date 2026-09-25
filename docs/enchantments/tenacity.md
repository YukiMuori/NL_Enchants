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
Trigger(s):        ~onDamaged
Cooldown:          1s internal
```

## Effect

The first hit in a window starts a 5s 'hardened' state. Any further hit while hardened grants Resistance I for 2/3s (by level) and refreshes the window.

## VFX

End-rod pulse + faint bell ring on each hardened hit.

## Balance

Rewards tanking sustained fights, does nothing vs burst. Resistance is short and only while the chain lives.

## Notes

Identity: SUSTAINED DEFENSE (stacks via aura refresh + expiration).

## Files

```text
enchantments/defensive/tenacity.yml
skills/defensive/tenacity.yml
vfx/defensive/tenacity.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
