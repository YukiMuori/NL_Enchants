# Resonance

```text
ID:                nl:resonance
Italian name:      Risonanza
English name:      Resonance
Category:          legendary
Rarity:            LEGENDARY
Maximum Level:     1
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         none
Trigger(s):        ~onDamaged (two gated dispatch lines) + ~onEquip (link VFX)
Cooldown:          20s per tier (metaskill cooldown)
```

## Effect

Attuned pieces respond when you are struck:

- **Full set** (all four slots hold `nl:resonance`, checked at damage time
  via four plain inline `?mench` conditions on the enchant line):
  Regeneration II for 8s + full ring pulse.
- **Otherwise** (any piece): Regeneration I for 3s + small pulse. The
  weaker potion never overrides the stronger (potion `force=false` default),
  and its VFX is suppressed while the full-set regen is active.

## VFX

End-rod pulse (any tier) / end-rod + glow ring (full set); amethyst chime;
link sparkle on equip.

## Balance

Reactive (on damaged), 20s cooldown per tier — not passive sustain. The
full-set check happens at event time on the enchant's direct line, so it is
always accurate. Graceful degradation: if the `?mench` gate ever failed to
load, the full tier is skipped and the base tier still works.

## Notes

- v0.3.1: slot checks moved OUT of MythicMobs skill files — MythicEnchants
  conditions fail to load there (field-verified). Rule R8.
- The old heartbeat/any-piece-count tiers were removed for reliability.

## Files

```text
enchantments/legendary/resonance.yml   (dispatch + slot gates)
skills/legendary/resonance.yml         (pure mechanics)
vfx/legendary/resonance.yml
```
