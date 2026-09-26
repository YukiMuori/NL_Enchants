# Shadowstep

```text
ID:                nl:shadowstep
Italian name:      Passo d'Ombra
English name:      Shadowstep
Category:          movement
Rarity:            RARE
Maximum Level:     2
Supported Items:   #minecraft:enchantable/foot_armor
Valid Slots:       FEET
Conflicts:         none
Trigger(s):        ~onDamaged (inline chance gate on the direct line)
Cooldown:          4s internal
```

## Effect

When struck, 20%/30% chance (level) to dissolve backward: a short shadow
dash (relative -Z hop), 1s of Resistance I, and a lingering afterimage.
Evasion identity — not a stat, a moment.

## VFX

Core `NL_VFX_SHADOW_DASH`: smoke + soul silhouette, 3-beat afterimage
trail, muffled enderman teleport.

## Balance

Fixed small hop (counterable), 4s cooldown, short resistance window.
MaxLevel 2 scales only the proc chance.

## Files

```text
enchantments/movement/shadowstep.yml
skills/movement/shadowstep.yml
skills/core/burst.yml
```
