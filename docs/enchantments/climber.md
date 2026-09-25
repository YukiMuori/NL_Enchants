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
Trigger(s):        ~onEquip listener auras (Paper OnInput components)
Cooldown:          —
```

## Effect

On ladders/vines: holding sprint climbs faster (+0.1 Y per input tick); pressing jump leaps off (+0.42 Y).

## VFX

Rare cloud wisp while sprint-climbing; soft shoot sound on leap.

## Balance

Controlled vertical mobility — climbables only (isClimbing gate), no flight. Same listener-aura architecture as double_jump.

## Notes

Identity: VERTICAL MOBILITY.

## Files

```text
enchantments/movement/climber.yml
skills/movement/climber.yml
vfx/movement/climber.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
