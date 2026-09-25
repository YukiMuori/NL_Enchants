# Grounded

```text
ID:                nl:grounded
Italian name:      Radicamento
English name:      Grounded
Category:          defensive
Rarity:            UNCOMMON
Maximum Level:     2
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         none
Trigger(s):        ~onEquip / ~onUnequip (attribute)
Cooldown:          —
```

## Effect

+20%/+40% Knockback Resistance per piece while worn (enchantattribute, ADD_NUMBER, applied/removed on equip/unequip).

## VFX

None — passive attribute enchantment, like vanilla protection.

## Balance

Multiple pieces stack (vanilla attribute stacking). Never reaches full immunity (4x II = 160% capped by the attribute engine at 1.0 = 100%: in practice reaching 100% requires 3+ II pieces — full immunity is possible and accepted as the set fantasy; tune down if it proves oppressive in PvP).

## Notes

Identity: STABILITY. No damage reduction — does not overlap protection.

## Files

```text
enchantments/defensive/grounded.yml
skills/defensive/grounded.yml
vfx/defensive/grounded.yml            (if the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
