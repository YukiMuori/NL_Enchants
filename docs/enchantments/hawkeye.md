# Hawkeye

```text
ID:                nl:hawkeye
Italian name:      Occhio di Falco
English name:      Hawkeye
Category:          ranged
Rarity:            RARE
Maximum Level:     2
Supported Items:   #minecraft:enchantable/bow
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onShoot ?bowtension{value=>0.9} (inline, direct lines)
Cooldown:          —
```

## Effect

Fully-drawn shots (tension above 0.9) fly harder: +0.75 arrow damage per level. REDESIGNED v0.3.0: the old draw-focus listeners were replaced by the official arrowbuff-on-shoot pattern with an inline bowtension gate — every piece is a documented example.

## VFX

Crit burst + deep twang on empowered release.

## Balance

Only rewards max-draw shots — patience is the skill expression.

## Notes

Identity: PRECISION.

## Files

```text
enchantments/ranged/hawkeye.yml
skills/ranged/hawkeye.yml            (when the logic lives in metaskills)
vfx/ranged/hawkeye.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
