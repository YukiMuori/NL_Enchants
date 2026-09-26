# Winged Leap (nl:double_jump)

```text
ID:                nl:double_jump  (ID kept for item compatibility)
Italian name:      Balzo Alato
English name:      Winged Leap
Category:          movement
Rarity:            EPIC
Maximum Level:     3
Supported Items:   #minecraft:enchantable/foot_armor
Valid Slots:       FEET
Conflicts:         none
Trigger(s):        ~onEquip (level-gated listeners) · onJump mechanic ·
                   OnInput component (jump key)
Cooldown:          1s input guard; charges expire 6s after each ground jump
```

## Effect

After a normal jump, pressing the jump key again while airborne performs an
extra **directional** leap — up + forward in the player's facing (relative
velocity +0.45 Y / +0.35 forward), like magic wings or an air dash.

```text
LEVEL I   = 1 extra jump
LEVEL II  = 2 extra jumps
LEVEL III = 5 extra jumps
```

Every ground jump re-arms all level charges (6s lifetime, refreshed).
Holding the jump key re-fires the input once per second — reads as
continuous wing flapping while charges last (documented behavior).

## VFX

- Extra jump: wing flap — cloud burst underfoot, side end-rod arcs,
  firework motes, layered flap+chime (core `NL_VFX_WING_FLAP`).
- Last available jump: large burst + wide ground ring + rising trail +
  stronger call (core `NL_VFX_WING_FINISH`).

ItemDisplay wing animation was evaluated and **deferred**: display summon
syntax is not verified for this context and cleanup guarantees cannot be
given. Particle arcs carry the identity without entity risk.

## Architecture

Level-matched equip dispatches (`?mench` inline on the enchant's direct
lines — R8) install the `onJump` arm listener and the `OnInput` input
listener. Charge auras `nl_winged_c1..c5` ARE the remaining-jump tokens:
self-expiring, one consumed per input, finisher detection by full-absence
check. Unequip removes every aura. No counters, no variables, no leak paths.

## Balance

EPIC rarity, weight 2, levels 22–44, anvil 7. Mobility/exploration
signature: vertical + forward reach, no combat invulnerability attached.
Predictable impulses (fixed vectors) keep it counterable in PvP.

## Notes

RUNTIME-VERIFY: multi-charge chain feel, holding-key flapping cadence,
relog re-equip (listener architecture), level-gate switching when swapping
boots between levels.

## Files

```text
enchantments/movement/double_jump.yml
skills/movement/double_jump.yml
skills/core/wings.yml · skills/core/burst.yml
```
