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
Trigger(s):        ~onUse (drawing) + ~onShoot
Cooldown:          —
```

## Effect

Drawing the bow while braced (on ground) builds a short-lived focus. Releasing a fully-drawn shot (tension > 0.9) with focus adds +1.5/+3 arrow damage (by level) and consumes the focus.

## VFX

Rare end-rod wisp while focusing; crit burst + deep twang on the empowered release.

## Balance

'Stationary' is approximated as on-ground while drawing. Focus expires in 2s of not drawing, so it cannot be banked.

## Notes

Identity: PRECISION. RUNTIME-VERIFY: ~onUse draw behavior.

## Files

```text
enchantments/ranged/hawkeye.yml
skills/ranged/hawkeye.yml
vfx/ranged/hawkeye.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
