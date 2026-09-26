# Bloom (nl:green_thumb)

```text
ID:                nl:green_thumb  (ID kept for item compatibility)
Italian name:      Fioritura
English name:      Bloom
Category:          farming
Rarity:            COMMON
Maximum Level:     3
Supported Items:   #minecraft:enchantable/mining (Primary: hoes)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onBlockBreak on crops/melons/pumpkins (material gates)
Cooldown:          none — chance-gated (5/10/15% by level)
```

## Effect

Harvesting may release an **expanding natural wave**: three growth rings
(radius 2 → 3 → 4, 4 ticks apart) pulse outward around you, bonemealing
every plant they touch — crops accelerate, grass pops flowers, the farm
breathes.

## VFX

Core `NL_VFX_BLOOM_WAVE`: composter + happy-villager motes riding the
rings, bone-meal patter + soft bell. Each ring also puffs as it expands.

## Balance

Identity: farming reward loop — harvest feeds growth. Bonemeal cannot
fully-grown crops, so the wave never wastes itself on the block you just
harvested. MaxLevel 3 scales only the chance.

## Files

```text
enchantments/farming/green_thumb.yml
skills/farming/green_thumb.yml
skills/core/ring.yml
```
