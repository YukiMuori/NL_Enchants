# Thor

```text
ID:                nl:thor
Italian:           Thor
Category:          combat
Source:            AdvancedEnchantments "Vanilla+" list
Trigger:           ~onAttack (chance 5+5%/lvl) — melee weapons only
Cooldown:          none
```

## Effect

Lightning strike dealing level damage.

Scoped to `#minecraft:enchantable/weapon` (swords per PrimaryItems): the
ME datapack cannot express a multi-tag `SupportedItems` list — it
serializes as one invalid `#[...]` string and crashes server boot (R11).

## VFX

Real lightning visual+sound.

## Files

```text
enchantments/combat/thor.yml
skills/combat/vanilla_plus.yml
```
