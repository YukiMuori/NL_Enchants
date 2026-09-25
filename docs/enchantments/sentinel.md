# Sentinella

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

When hostiles are within 12 blocks (documented multi-type condition), your helm pulses with glow motes and a soft chime. REDESIGNED v0.3.0: self-centered feedback (per-mob marking used an unverified targeter).

## VFX

Self-centered glow pulse + quiet chime.

## Balance

Awareness only — no buffs, no marking.

## Notes

Identity: AWARENESS.

## Files

```text
enchantments/exploration/sentinel.yml
skills/exploration/sentinel.yml            (when the logic lives in metaskills)
vfx/exploration/sentinel.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
