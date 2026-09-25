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

While actively traveling (moving, outdoors, grounded), each minute grants Regeneration II for 3s.

## VFX

Happy-villager motes + soft levelup chime.

## Balance

Rewards the journey, not idling.

## Notes

Identity: EXPLORATION REWARD.

## Files

```text
enchantments/exploration/wayfarer.yml
skills/exploration/wayfarer.yml            (when the logic lives in metaskills)
vfx/exploration/wayfarer.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
