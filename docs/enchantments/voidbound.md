# Voidbound

```text
ID:                nl:voidbound
Italian name:      Vincolato al Vuoto
English name:      Voidbound
Category:          legendary
Rarity:            MYTHIC
Maximum Level:     1
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         nl:second_wind
Trigger(s):        ~onDamaged ?lethalcheck (official inline pattern)
Cooldown:          600s internal
```

## Effect

When the current damage event would kill you (totem-aware), the event is fully negated (reducedamage cap=1) and you gain Absorption II for 10s.

## VFX

Implosion drama: sculk-soul + portal burst, respawn-anchor charge + sculk undertone.

## Balance

Last resort: 10-minute cooldown, one charge, totem priority preserved. Never a replacement for skill.

## Notes

Identity: LAST RESORT.

## Files

```text
enchantments/legendary/voidbound.yml
skills/legendary/voidbound.yml
vfx/legendary/voidbound.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
