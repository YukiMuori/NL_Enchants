# Catalog plan — v0.5.0 "Vanilla+" port

Source list: [AdvancedEnchantments — Vanilla+ enchants](https://ae.advancedplugins.net/enchantments/list-of-enchantments/vanilla-enchants).

Method (rule R6): every AE enchant was checked against the mechanics
**verified** on the official MythicMobs / MythicEnchants docs (see the
verified-facts table in `docs/development.md`). Feasible enchants ship;
the rest are listed in
[`_skipped-from-ae-list.md`](_skipped-from-ae-list.md) with the exact
missing mechanic. Nothing was invented to close a gap.

## Shipped (38 enchants, 6 categories)

| Category | Enchants |
| --- | --- |
| combat | `nl:arctic_freeze` (Arctic Freeze 3), `nl:blackout` (Blackout 5), `nl:double_blow` (Double Blow 4), `nl:drain` (Drain 7), `nl:enderbane` (Enderbane 5), `nl:zombie_crusher` (Zombie Crusher 3), `nl:skullcrusher` (Skullcrusher 3), `nl:incinerate` (Incinerate 3), `nl:blaze_reaper` (Blaze Reaper 3), `nl:cubism` (Cubism 3), `nl:first_strike` (First Strike 3), `nl:finishing` (Finishing 3), `nl:postpone` (Postpone 3), `nl:repel` (Repel 3), `nl:starvation` (Starvation 3), `nl:thor` (Thor 3), `nl:ninja` (Ninja 3), `nl:ravenous` (Ravenous 4) |
| ranged | `nl:multi_shot` (Multi-Shot 3), `nl:flashbang` (Flashbang 3), `nl:frost` (Frost 3), `nl:explosive` (Explosive 5) |
| mining | `nl:blast_mining` (Blast Mining 3), `nl:experience` (Experience 5), `nl:foraging` (Foraging 3), `nl:nether_prospector` (Nether Prospector 3), `nl:haste` (Haste 3) |
| defensive | `nl:adrenaline` (Adrenaline 3), `nl:end_affinity` (End Affinity 3), `nl:nether_affinity` (Nether Affinity 3), `nl:rebounding` (Rebounding 3), `nl:rumble` (Rumble 3), `nl:scorching` (Scorching 3), `nl:vanish` (Vanish 3), `nl:waterborne` (Waterborne 1) |
| movement | `nl:escape` (Escape 2), `nl:feather_step` (Feather Step 5) |
| farming | `nl:replenish` (Replenish 1) |

Documented adaptations (no mechanic invented, only scaled):

- **Double Blow** — AE repeats the attack; we deal a flat extra hit
  (level+2) with crit feedback. `item_attack` inside metaskills is not
  guaranteed resolvable (R1), so no damage-scaled second blow.
- **Ninja** — AE checks sneaking on hit; we use the verified OnInput
  component (`requiresneak=true`) to arm a short-lived sneak token.
- **Waterborne** — refresh is not water-gated: no verified in-block
  condition; on land Water Breathing has no visible effect.
- **Haste** absorbs AE **Alacrity** (same effect) — no duplicate (rule).
- **Escape** absorbs AE **Getaway** — same low-HP speed idea, one ID.
- **Explosive** uses `fakeexplosion` (official visual-only mechanic) plus
  its own damage: we never block damage.
- **End/Nether Affinity** gate on world names — defaults cover common
  names; see SETUP.md to adjust to your server.

## Skipped (see `_skipped-from-ae-list.md` for per-enchant reasons)

Bane-family variants beyond the shipped ones, fishing enchants, XP-grant
and drop-multiplier where unverified, inventory manipulation, crit
detection, curse event-canceling, right-click activators, and others —
all blocked by a named missing mechanic, not by choice.
