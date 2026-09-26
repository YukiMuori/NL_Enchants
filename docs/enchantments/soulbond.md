# Soulbond

```text
ID:                nl:soulbond
Italian name:      Anima Gemella
English name:      Soulbond
Category:          legendary
Rarity:            LEGENDARY
Maximum Level:     1
Supported Items:   #minecraft:enchantable/armor
Valid Slots:       HEAD, CHEST, LEGS, FEET
Conflicts:         none
Trigger(s):        ~onDeath (recoveritem) + ~onEquip (link VFX)
Cooldown:          none — per-item 3 charges (persistent on the item)
```

## Effect

Each bonded piece protects **itself** on death: the item stays with you and
is re-equipped, up to **3 times** per item (charges stored persistently on
the item). Wearing the full set naturally protects the whole outfit — each
piece with its own charge count.

## VFX

End-rod + soul motes and a chime when the bond is established on equip.

## Balance

Built exactly on the official `RecoverItem` enchant example
(`recoveritem{slot=TRIGGER;limit=3;reequip=true} @trigger ~onDeath`).
Charges persist on the item across deaths; no cross-slot state, no cleanup.

## Notes

- v0.3.1: the outfit-web extension (cross-slot `hasMythicEnchant` checks
  inside a MythicMobs skill file) failed to load in-game and was removed.
  Per-piece protection achieves the same end result with zero risk.
- RUNTIME-VERIFY: confirm `reequip=true` restores the piece to its slot.

## Files

```text
enchantments/legendary/soulbond.yml    (official recoveritem line)
vfx/legendary/soulbond.yml
```
