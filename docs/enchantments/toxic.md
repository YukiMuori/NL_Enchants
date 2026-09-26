# Toxic

```text
ID:                nl:toxic
Italian:           Tossico
Category:          ranged
Source:            Vanilla+ utility list (server owner request)
Trigger:           ~onBowHit (always)
Cooldown:          none
```

## Effect

Arrows poison the victim for 11 seconds. Undead (zombie/skeleton families, Wither, Phantom…) are immune via an entitytype gate.

## VFX

Server-side effect particles + wither-shoot hiss on proc.

## Notes

- BOW ONLY: bow+crossbow would need two SupportedItems tags in one list — illegal (R11). A crossbow variant would need a separate ID.

## Files

```text
enchantments/ranged/toxic.ymlentitytype gate @metaskill NL_TOXIC_HIT
```
