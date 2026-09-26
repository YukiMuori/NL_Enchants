# Scorch Walker

```text
ID:                nl:scorch_walker
Italian:           Passo Ardente
Category:          movement
Source:            Vanilla+ utility list (server owner request)
Trigger:           ~onEquip aura (2-tick) + ~onDamaged gates
Cooldown:          none
```

## Effect

Places a magma block at your feet while you are inside lava (blocktype-gated aura tick) — you can cross lava lakes walking on it. Also fully negates magma-block damage (HOT_FLOOR) and powder-snow freeze damage; L2 additionally negates lava contact damage.

## VFX

Small flame motes while generating blocks.

## Notes

- ADAPTATION: no frost-walker-style surface generation exists in verified mechanics — one block under the feet only. Placed magma persists (vanilla-like). RUNTIME-VERIFY: aura tick cadence + blocktype condition.

## Files

```text
enchantments/movement/scorch_walker.ymlaura components @NL_SCORCH_TICK
```
