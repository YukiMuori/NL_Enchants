# Climber

```text
ID:                nl:climber
Italian name:      Scalatore
English name:      Climber
Category:          movement
Rarity:            UNCOMMON
Maximum Level:     1
Supported Items:   #minecraft:enchantable/foot_armor
Valid Slots:       FEET
Conflicts:         none
Trigger(s):        ~onEquip listener auras (OnInput components)
Cooldown:          —
```

## Effect

On ladders/vines: holding sprint climbs faster; pressing jump leaps off.

## VFX

Rare cloud wisp while sprint-climbing; soft shoot sound on leap.

## Balance

Climbables only (isClimbing gate).

## Notes

Identity: VERTICAL MOBILITY. Listener-aura architecture — re-equip after relog.

## Files

```text
enchantments/movement/climber.yml
skills/movement/climber.yml            (when the logic lives in metaskills)
vfx/movement/climber.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
