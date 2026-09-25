# Staggering

```text
ID:                nl:staggering
Italian name:      Barcollante
English name:      Staggering
Category:          combat
Rarity:            RARE
Maximum Level:     2
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         nl:sluggish
Trigger(s):        ~onAttack
Cooldown:          —
```

## Effect

On hit: 10/14% chance to lift the target slightly and pin it in place for ~0.3s (repeated zero-velocity).

## VFX

Crit particle burst + iron golem impact sound on the target.

## Balance

Physical interruption — no slow, no damage. Conflicts with sluggish (control group). Short root keeps PvP fair.

## Notes

Identity: INTERRUPTION / PHYSICAL CONTROL.

## Files

```text
enchantments/combat/staggering.yml
skills/combat/staggering.yml
vfx/combat/staggering.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
