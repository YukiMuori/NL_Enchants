# Mark

```text
ID:                nl:mark
Italian name:      Marchio
English name:      Mark
Category:          combat
Rarity:            RARE
Maximum Level:     1
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onAttack → metaskills @target
Cooldown:          —
```

## Effect

First hit marks a target for 8s. Subsequent hits on the marked target deal +1.5 bonus damage and refresh the mark.

## VFX

Glow motes on application; end-rod pulse per rewarded hit.

## Balance

Single-target focus state. MaxLevel 1.

## Notes

Identity: COMBO / TARGET STATE.

## Files

```text
enchantments/combat/mark.yml
skills/combat/mark.yml            (when the logic lives in metaskills)
vfx/combat/mark.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
