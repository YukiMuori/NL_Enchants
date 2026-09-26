# Combo

```text
ID:                nl:combo
Italian name:      Combo
English name:      Combo
Category:          combat
Rarity:            RARE
Maximum Level:     3
Supported Items:   #minecraft:enchantable/weapon (Primary: #minecraft:swords)
Valid Slots:       MAINHAND
Conflicts:         none
Trigger(s):        ~onAttack (direct lines, MythicEnchants counter)
Cooldown:          none — 4s chain window (counter expiry refreshes per hit)
```

## Effect

Consecutive hits within 4 seconds build a combo with escalating feedback:
hit 1–3 show growing spark/chime tiers, the **4th hit is a finisher**
(+1/+2/+3 damage by level, core impact VFX) and resets the chain. Stop
hitting for 4s and the combo decays to zero.

## VFX

Tier 1: small crit sparks. Tier 2: bigger sparks + pickup chime.
Tier 3: end-rod + hat note. Finisher: flash + crit burst + crit sound
(core `NL_VFX_IMPACT`).

## Balance

Identity: rhythm reward. Damage total is modest (finisher only); the
escalating audiovisual chain is the real payoff. Counter is player-scoped
with 4s expiry — switching targets keeps the chain (flow over tankiness).

## Notes

- Pattern: `addcounter`/`?counter` driven entirely on the enchant's DIRECT
  lines (official Counter usage; inline conditions on enchant lines are the
  official pattern — R8/R4 compliant).

## Files

```text
enchantments/combat/combo.yml
skills/combat/combo.yml               (finisher damage)
skills/vfx/combat/combo.yml           (tier feedback)
resourcepack/assets/minecraft/lang/{en_us,it_it}.json
```
