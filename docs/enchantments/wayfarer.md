# Wayfarer

```text
ID:                nl:wayfarer
Italian name:      Viandante
English name:      Wayfarer
Category:          exploration
Rarity:            UNCOMMON
Maximum Level:     1
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         none
Trigger(s):        ~onEquip listener aura (5s heartbeat)
Cooldown:          60s internal
```

## Effect

While actively traveling (moving, outdoors, on ground), each minute of honest exploration grants Regeneration II for 3s.

## VFX

Happy-villager motes + soft levelup chime.

## Balance

Rewards the JOURNEY (continuous movement outdoors), not idling or cave time. 60s internal cooldown.

## Notes

Identity: EXPLORATION REWARD. Designed from the intentionally-underspecified master concept.

## Files

```text
enchantments/exploration/wayfarer.yml
skills/exploration/wayfarer.yml
vfx/exploration/wayfarer.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
