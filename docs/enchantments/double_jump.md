# Double Jump

```text
ID:                nl:double_jump
Italian name:      Doppio Salto
English name:      Double Jump
Category:          movement
Rarity:            RARE
Maximum Level:     1
Supported Items:   #minecraft:enchantable/foot_armor
Valid Slots:       FEET
Conflicts:         none
Trigger(s):        ~onEquip, ~onUnequip (MythicEnchants equipment triggers)
                   + Paper jump event + player jump-key input (runtime listeners)
Cooldown:          none (activation is deliberate input; a 1s internal guard
                   exists on the input handler to absorb input spam)
```

## Effect

One sentence:

> After jumping, press the jump key again while airborne to leap a second time.

Details:

- Every **real ground jump** arms a self-expiring 5-second *charge*.
- While the wearer is airborne and the charge is held, pressing (or holding)
  the jump key consumes the charge and applies **one** additional
  vanilla-strength upward impulse (`+0.42 Y`, identical to a vanilla jump),
  for a total height of roughly two blocks.
- The charge expires 5 s after the jump, so it can never be banked for later
  (e.g. jumping, landing, then floating off a ledge).
- Players who habitually *hold* space through a jump will trigger the second
  impulse right after the first jump — it simply reads as a slightly stronger
  jump. Tapping jump twice gives the crisp two-beat double jump.

## VFX

Defined in `vfx/movement/double_jump_vfx.yml` (`NL_VFX_DOUBLEJUMP_BURST`):

- `cloud` puff beneath the feet (12 particles)
- rising `end_rod` motes (10 particles)
- layered audio: `entity.ender_dragon.flap` (airy whoosh, pitched up) +
  `entity.experience_orb.pickup` (faint chime)

Fires only on activation — no idle particles, no passive visuals.

## Balance notes

- MaxLevel is intentionally 1 — there is no meaningful scaling for a
  binary movement ability.
- No cooldown by design: activation costs a deliberate second key press and
  one charge per ground jump, which self-limits usage to roughly the natural
  jump cadence. A 1-second internal guard on the input handler absorbs
  key-repeat spam.
- The impulse matches vanilla jump strength (+0.42). It is a mobility and
  exploration tool, not an evasion multiplier: the fixed 3-tick settle delay
  and ground check make it predictable in PvP rather than an instant dodge.
- Obtainability: enchanting-table weight 4 (RARE band), levels 18–42,
  anvil cost 6, tradeable and lootable (defaults).

## Implementation notes & design rationale

Paper fires its jump event only when a jump **starts from the ground**; a
mid-air press of the jump key produces no server-side event. A literal
"second jump" therefore cannot hook the key press directly.

The pack instead combines two documented MythicMobs features (both
Paper-only, which is already a hard requirement of MythicEnchants):

1. `onJump` aura mechanic — fires a skill on each real ground jump.
   That skill grants the short-lived `nl_dj_charge` aura (the token).
2. `OnInput` aura component with `requirejump=true` — observes the player's
   jump **input state** each tick; when it matches while airborne, the token
   is consumed and the impulse fires.

The token is an aura (not a persistent variable), so it is self-expiring and
cannot leak: unequipping the boots removes every aura this enchantment can
create (`nl_dj_arm`, `nl_dj_input`, `nl_dj_charge`).

Known limitations (verify at runtime):

- After a **relog**, listener auras are dropped (MythicMobs cleans up on
  quit). Re-equipping the boots restores them. If MythicEnchants re-fires
  `~onEquip` at login, this resolves automatically — confirm on the live
  server and update this file.
- The jump-key input is a *state* (down/up), not an edge, so holding space
  from the first jump also triggers the second impulse. This is intentional
  and documented above.

## Performance assessment

- Two long-lived listener auras per wearer: one is purely event-driven
  (`onJump`), the other is a per-tick input-state check (`i=1`) — a cheap
  state read, no world/entity scans.
- One 5-second charge aura per ground jump, capped at one stack.
- VFX fire only on activation: 22 particles + 2 sounds.
- No spawned entities, no timers, no radius searches, no cleanup risk.

## Files

```text
enchantments/movement.yml             → nl:double_jump definition (thin dispatcher)
skills/movement/double_jump.yml       → NL_ENCHANT_DOUBLEJUMP_* logic chain
vfx/movement/double_jump_vfx.yml      → NL_VFX_DOUBLEJUMP_BURST
resourcepack/assets/minecraft/lang/   → en_us / it_it name + description
```
