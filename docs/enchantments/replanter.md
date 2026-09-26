# Replanter

```text
ID:                nl:replanter
Italian name:      Ripiantatore
English name:      Replanter
Category:          farming
Rarity:            COMMON
Maximum Level:     1
Supported Items:   #minecraft:enchantable/mining (Primary: hoes)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onEquip listeners (OnBlockBreak aura components)
Cooldown:          none — QoL
```

## Effect

Harvested crops are instantly replanted (age 0). One documented
`OnBlockBreak` aura component per crop (wheat, carrots, potatoes,
beetroots): the component's blocktypes filter does the gating and
`@targetlocation` is the broken block — the exact semantics of the
official example. Drops still pop (component `dropitem` default true).

## Balance / Notes

- v0.4.0 rewrite: the previous direct `setblock` + `triggerblocktype`
  lines never fired in the field; this version uses only documented
  component behavior.
- Listener architecture: active while the hoe is held; re-equip after
  relog (RUNTIME-VERIFY).

## Files

```text
enchantments/farming/replanter.yml
skills/farming/replanter.yml
```
