# Momentum

```text
ID:                nl:momentum
Italian name:      Impeto
English name:      Momentum
Category:          combat
Rarity:            UNCOMMON
Maximum Level:     3
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onKill → metaskill @self
Cooldown:          —
```

## Effect

Kills grant a 5s Momentum stack (max 5) and Speed I for 5s. Taking any damage breaks the chain. (v0.3.0: fixed Speed I — level scaling removed for reliability.)

## VFX

Firework motes + chime per kill; fading puff when broken.

## Balance

Rewards clean chains. Speed never exceeds 5s / one amplifier.

## Notes

Identity: COMBAT FLOW.

## Files

```text
enchantments/combat/momentum.yml
skills/combat/momentum.yml            (when the logic lives in metaskills)
vfx/combat/momentum.yml               (when the enchant has active VFX)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
