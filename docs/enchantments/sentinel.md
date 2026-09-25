# Sentinel

```text
ID:                nl:sentinel
Italian name:      Sentinella
English name:      Sentinel
Category:          exploration
Rarity:            RARE
Maximum Level:     1
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD
Conflicts:         none
Trigger(s):        ~onEquip listener aura (5s heartbeat)
Cooldown:          one scan / 5s
```

## Effect

When hostiles are within 12 blocks, up to 4 of the nearest get a subtle glow mote and you hear a soft amethyst chime.

## VFX

Glow particles above hostiles + quiet chime. Subtle by design.

## Balance

Awareness only — no reveal through walls beyond particles, no buffs. Performance: one capped radius check every 5s per wearer.

## Notes

Identity: AWARENESS. RUNTIME-VERIFY: @MobsInRadius types filter + hostile list coverage.

## Files

```text
enchantments/exploration/sentinel.yml
skills/exploration/sentinel.yml
vfx/exploration/sentinel.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
