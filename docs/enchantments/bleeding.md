# Hemorrhage (nl:bleeding)

```text
ID:                nl:bleeding  (ID kept for item compatibility)
Italian name:      Emorragia
English name:      Hemorrhage
Category:          combat
Rarity:            UNCOMMON
Maximum Level:     3
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onAttack → target-state chain
Cooldown:          none — marks decay after 4s each
```

## Effect

Consecutive hits on the same target build wounds:

```text
HIT 1 → mark I        (small sting particles)
HIT 2 → mark II       (bigger sting)
HIT 3 → BURST         (1 dmg/s for 3s, then a final 2-damage tear + blood burst)
```

Marks are distinct aura states on the target (4s lifetime each, refreshed
per hit); the burst clears them and the chain restarts. Switching targets
starts a fresh chain (per-target state by design).

## VFX

Blood feedback per stage; the burst ends with the core `NL_VFX_BLOOD_HIT`
(damage indicators + redstone spray + wet tear sound).

## Balance

Identity: buildup damage-over-time. Total burst damage is 5 (3 DoT + 2
end) regardless of level — level currently expresses availability
(enchanting level band), keeping PvP numbers predictable. MaxLevel 3 kept
for future tuning hooks.

## Files

```text
enchantments/combat/bleeding.yml
skills/combat/bleeding.yml
skills/core/burst.yml
```
