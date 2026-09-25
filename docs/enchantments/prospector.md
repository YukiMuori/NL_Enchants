# Prospector

```text
ID:                nl:prospector
Italian name:      Prospezione
English name:      Prospector
Category:          mining
Rarity:            RARE
Maximum Level:     1
Supported Items:   #minecraft:enchantable/pickaxe
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onBlockBreak (one gate line per ore tag)
Cooldown:          6s internal
```

## Effect

Mining any ore sends out a pulse: a strong chime if DIAMOND ore lies within 8 blocks, a soft tick otherwise. REDESIGNED v0.3.0 (Diamond Sense) — exact-position reveal of arbitrary ores requires Premium inline targeter conditions (out of scope).

## VFX

Tiered end-rod/glow sparkle + chime vs quiet tick.

## Balance

Information enchant; does not change drops.

## Notes

Identity: INFORMATION / EXPLORATION.

## Files

```text
enchantments/mining/prospector.yml
skills/mining/prospector.yml            (when the logic lives in metaskills)
vfx/mining/prospector.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
