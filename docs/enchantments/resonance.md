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
Trigger(s):        ~onEquip listener aura (8s heartbeat) + ~onUnequip
Cooldown:          one pulse / 8s
```

## Effect

TWO tiers (v0.3.0 simplification): ANY piece = Regeneration I 3s; FULL set = Regeneration II 8s. Full set is four plain conditions (no composite chains); the any-piece tier uses one documented composite OR.

## VFX

End-rod pulse (any) / end-rod + glow ring (full).

## Balance

Full-set potion applies first; the weaker any-tier potion respects it (potion force=false default).

## Notes

Identity: SET / SYNERGY.

## Files

```text
enchantments/legendary/resonance.yml
skills/legendary/resonance.yml            (when the logic lives in metaskills)
vfx/legendary/resonance.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
