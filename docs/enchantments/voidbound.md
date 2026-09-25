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

When the current damage event would kill you (totem-aware), it is fully negated (reducedamage a=1000, cap=1 — no damage variable needed) and you gain Absorption II for 10s.

## VFX

Implosion drama: sculk-soul + portal burst, anchor charge + sculk undertone.

## Balance

Last resort: 10-minute cooldown, totem priority preserved.

## Notes

Identity: LAST RESORT.

## Files

```text
enchantments/legendary/voidbound.yml
skills/legendary/voidbound.yml            (when the logic lives in metaskills)
vfx/legendary/voidbound.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
