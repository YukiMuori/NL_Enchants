# Balancing

Values are in the enchant files only — never changed silently; changes
require a version bump and a CHANGELOG entry.

## Rarity bands

| Rarity | Weight | MinCost | MaxCost | Anvil |
| --- | --- | --- | --- | --- |
| COMMON | 6 | 4 | 24 | 1 |
| UNCOMMON | 5 | 8 | 30 | 2 |
| RARE | 3 | 16 | 38 | 4 |

## Per-enchant values (v0.5.0)

| Enchant | Levels | Core numbers |
| --- | --- | --- |
| `nl:thor` | 3 | 5+5%/lvl chance, level dmg |
| `nl:drain` | 7 | 12% chance; level+1 dmg, level heal |
| `nl:arctic_freeze` | 3 | 5+5%/lvl; Slow 3s + 3×1 bleed |
| `nl:blackout` | 5 | 4+4%/lvl; Blind 2s |
| `nl:double_blow` | 4 | 10+5%/lvl; flat +lvl+2 |
| `nl:first_strike` | 3 | +1+lvl if target >95% HP |
| `nl:finishing` | 3 | +1+lvl if target <30% HP |
| `nl:postpone` | 3 | 10+10%/lvl; velocity=0 |
| `nl:repel` | 3 | 8+8%/lvl; knock 0.4y/−0.6z |
| `nl:starvation` | 3 | 8+8%/lvl; Hunger 5s |
| `nl:ravenous` | 4 | 10+10%/lvl; +lvl+1 food |
| `nl:ninja` | 3 | +1+lvl while sneaking |
| bane family (`enderbane` `zombie_crusher` `skullcrusher` `incinerate` `blaze_reaper` `cubism`) | 3–5 | +1–2 flat by level, type-gated |
| `nl:multi_shot` | 3 | 25%; 1+lvl arrows, spread 20 |
| `nl:flashbang` | 3 | 15+15%/lvl; Blind 3s |
| `nl:frost` | 3 | 10+10%/lvl; freeze 1.5s+lvl×1s |
| `nl:explosive` | 5 | 8+8%/lvl; fakeexplosion + lvl+1 dmg |
| `nl:blast_mining` | 3 | 34%/lvl; 3×3×3, cap 2+2×lvl, per-block 2 durability |
| `nl:experience` | 5 | 10+10%/lvl XP bottle on ores |
| `nl:foraging` | 3 | 15+15%/lvl stick+sapling |
| `nl:nether_prospector` | 3 | 10+10%/lvl extra debris |
| `nl:haste` | 3 | Haste I while held (2s heartbeat) |
| `nl:adrenaline` | 3 | 15+15%/lvl; Strength I 4s, hostiles only |
| `nl:end/nether_affinity` | 3 | 15%/lvl reduction, cap 50%, world-gated |
| `nl:rebounding` | 3 | reduce 10%/lvl (cap 30%), reflect 20%/lvl |
| `nl:rumble` | 3 | 10+10%/lvl; lvl+1 AoE r=3, mobs only |
| `nl:scorching` | 3 | 15%; ignite 1s+lvl×1s |
| `nl:vanish` | 3 | 4+4%/lvl, 10s CD; Invis 3s |
| `nl:escape` | 2 | 30%, 8s CD; Speed I 3s |
| `nl:feather_step` | 5 | 20+16%/lvl full fall cancel |
| `nl:waterborne` | 1 | Water Breathing refresh 5s |
| `nl:replenish` | 1 | mature crops replant; immature untouched |

## Design rules kept from the rework

- One sentence per enchant; short reactive mechanics over long states.
- Cooldowns on defensive procs (Vanish 10s, Escape 8s).
- Rumble never hits players; bane bonuses are flat, not multiplicative.
- Blast Mining scales by level via proc chance (34/68/100%), not radius —
  radius jumps are a bigger feel spike than frequency jumps.
