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
Trigger(s):        ~onDamaged → hostile-presence gated glow ping
Cooldown:          5s internal
```

## Effect

When you are hit **and** hostiles lurk within 10 blocks, every nearby
hostile (up to 12) is pinned with a **glowing outline for 5 seconds** —
the dark cannot hide what struck you. Soft amethyst chime marks the pulse.

## VFX

Vanilla glow outline on each marked hostile (readable through the fray),
single quiet chime. No particle spam.

## Balance

Identity: awareness/reveal on being attacked — defensive information,
no buffs. 5s cooldown aligns with the glow duration (near-continuous
revelation during sustained fights, nothing while exploring peacefully).

## Notes

RUNTIME-VERIFY (flagged): the `@MobsInRadius` types filter and the plain
`glow` aura component are documented but unproven in this exact context.
**Verified fallback** (if the targeter filter misbehaves): keep the
verified `mobsinradius` condition gate and replace the marking with a
self-centered pulse (`glow` motes + chime). Report which one the server
uses.

## Files

```text
enchantments/exploration/sentinel.yml
skills/exploration/sentinel.yml
```
