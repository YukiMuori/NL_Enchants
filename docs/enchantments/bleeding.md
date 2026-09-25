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
Trigger(s):        ~onAttack → metaskill @target
Cooldown:          —
```

## Effect

On hit: 5/10/15% chance to open a wound: 1 damage (half heart) per second for 4s.

## VFX

Damage-indicator particles per tick; redstone dust burst on end.

## Balance

True damage-over-time identity. Tick skill uses constants only (variables do not survive into aura tick context).

## Notes

Identity: DAMAGE OVER TIME.

## Files

```text
enchantments/combat/bleeding.yml
skills/combat/bleeding.yml            (when the logic lives in metaskills)
vfx/combat/bleeding.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
