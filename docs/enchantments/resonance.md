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

Piece-count synergy (exact-count conditions via hasMythicEnchant per slot): 1 piece = Regen I 2s; 2 = Regen I 4s; 3 = Regen II 4s; 4 = Regen II 8s + full ring pulse.

## VFX

End-rod rings scaling by tier; amethyst chime; glow ring on the full set.

## Balance

Set/synergy identity. Drift-free counting (no stored state — recomputed each pulse from real equipment). Regen is the full effect: modest even at 4 pieces.

## Notes

Identity: SET / SYNERGY.

## Files

```text
enchantments/legendary/resonance.yml
skills/legendary/resonance.yml
vfx/legendary/resonance.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
