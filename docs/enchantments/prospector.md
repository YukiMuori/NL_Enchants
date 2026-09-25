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
Trigger(s):        ~onBlockBreak
Cooldown:          6s internal
```

## Effect

Mining a valuable ore sends out a pulse whose strength (3 tiers) grows with how many valuable ores lie within 8 blocks.

## VFX

End-rod/glow sparkle + chime, escalating by tier.

## Balance

Information enchant — reveals PRESENCE/intensity, not ore positions (per-block reveal requires Premium inline targeter conditions; deliberately avoided). Does NOT change drops.

## Notes

Identity: INFORMATION / EXPLORATION. Design deviation documented.

## Files

```text
enchantments/mining/prospector.yml
skills/mining/prospector.yml
vfx/mining/prospector.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
