# Retrieval

```text
ID:                nl:retrieval
Italian:           Recupero
Category:          defensive
Source:            Vanilla+ utility list (server owner request)
Trigger:           ~onDamaged by projectiles (chance 20%/lvl)
Cooldown:          none
```

## Effect

When hit by an arrow, chance to receive an arrow directly into your inventory (20/40/60/80%), with the fake-looting pickup animation.

## VFX

fakeLooting item fly-in animation (giveitem).

## Notes

- ADAPTATION: the arrow that hit still drops normally — the enchant adds a retrieved arrow on top; tipped-arrow effects are not replicated (documented). giveitem is a verified MM mechanic.

## Files

```text
enchantments/defensive/retrieval.yml—
```
