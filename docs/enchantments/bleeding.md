# Bleeding

```text
ID:                nl:bleeding
Italian name:      Sanguinante
English name:      Bleeding
Category:          combat
Rarity:            UNCOMMON
Maximum Level:     3
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onAttack
Cooldown:          —
```

## Effect

On hit: 12% chance to open a wound: 1 damage (half heart) per second for 3/4/5s (by level). Ends with a final burst.

## VFX

Damage-indicator particles per tick; redstone dust burst + sweet-berry hurt sound on end.

## Balance

True damage-over-time identity, distinct from sluggish (control) and staggering (interruption). Fixed 12% keeps it predictable.

## Notes

Identity: DAMAGE OVER TIME.

## Files

```text
enchantments/combat/bleeding.yml
skills/combat/bleeding.yml
vfx/combat/bleeding.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
