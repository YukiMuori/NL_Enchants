# In-Game Testing Protocol

**Static validation ≠ runtime validation.** This is the checklist for
runtime verification on Paper + MythicMobs + MythicEnchants. Nothing is
"done" until it passes here.

## Before you start

1. Install the pack (`SETUP.md`), restart **twice** (enchant registration
   needs a full restart; skill edits only need `/mm reload`).
2. Keep the **console open** — failed skill lines print errors there.
3. Grant test items with `/enchant @s <id> <level>`.
4. `nl:end_affinity` / `nl:nether_affinity`: first edit the `?world{w=...}`
   lists to your server's world names (SETUP.md).

Report back, for each enchant: WORKS / FAILS + the exact console error
lines (if any) + one sentence about the feel (too strong/weak/often).

## Per-enchant test matrix

| Enchant | Test | Expected |
| --- | --- | --- |
| `nl:thor` | L1–L3, hit mobs ~30×; also with a bow | occasional real lightning (level damage); no fire grief (does it ignite? verify) |
| `nl:drain` | hit ~10× | heals on ~12% of hits; no overheal beyond max |
| `nl:arctic_freeze` | hit ~15× | Slowness + 1/s bleed for 3s on proc; snowflakes |
| `nl:blackout` | hit ~20× L1 vs L5 | brief blindness, freq scales with level |
| `nl:double_blow` (trident) | throw/sweep ~15× | extra crit-hit every ~5–7 attacks |
| `nl:first_strike` | hit full-HP vs wounded mob | bonus only on the opening hit |
| `nl:finishing` | finish wounded mobs | bonus under 30% HP + sparks |
| `nl:postpone` | hit ~10× | occasionally the mob barely moves |
| `nl:repel` | hit ~10× | occasional up+back fling with ram sound |
| `nl:starvation` | hit ~10× (creative test on player) | hunger icon sometimes |
| `nl:ravenous` | fight with low hunger bar | refills ~1 in 10 hits |
| `nl:enderbane` / `nl:zombie_crusher` / `nl:skullcrusher` / `nl:incinerate` / `nl:blaze_reaper` / `nl:cubism` | hit the right mobs vs wrong ones | bonus + VFX only on listed types |
| `nl:ninja` | sneak-attack vs normal attacks | bonus + smoke only on sneak hits; no state left after unequip |
| `nl:ravenous` | — | (row above) |
| `nl:multi_shot` | shoot ~10× | 1-in-4 arrow volley; volley arrows not pickable |
| `nl:flashbang` | shoot ~10× | blindness + flash on proc |
| `nl:frost` | shoot ~10× | powder-snow freeze (can't move) on proc |
| `nl:explosive` | shoot ~10× | big puff + damage + never destroys blocks |
| `nl:blast_mining` | mine stone/dirt with L1–L3 pick; also inside a claim | 3×3 wave on ~34%/level; claims can veto (verify) |
| `nl:experience` | mine ~10 ores | occasional XP bottle |
| `nl:foraging` | break ~10 leaf blocks | occasional stick+sapling |
| `nl:nether_prospector` | mine ~10 debris | occasional double debris |
| `nl:haste` | hold tool vs swap away | haste while held, gone after unequip; RUNTIME-VERIFY mainhand equip semantics |
| `nl:adrenaline` | let mobs hit you | Strength I sometimes; no proc vs fall |
| `nl:rebounding` | melee mob hits you | reduced damage + reflected hit |
| `nl:rumble` | get hit surrounded by mobs | AoE hit on ~10%/level |
| `nl:scorching` | let mobs hit you | attacker ignites on 15% |
| `nl:vanish` | take hits | rare 3s invisibility, ≥10s between |
| `nl:waterborne` | helmet on, dive | bubbles never drop |
| `nl:escape` | take hits | 3s Speed on 30%, ≥8s between |
| `nl:feather_step` | fall from height repeatedly | fall cancel ~20+16%/level |
| `nl:replenish` | break crops: mature and immature | mature replants instantly; immature NEVER replants (must drop normally) |

## Architecture-level checks (gate several enchants)

- **Listener-aura enchants** (`nl:ninja`, `nl:haste`, `nl:replenish`,
  `nl:waterborne`) after a **relog**: auras may be cleaned on quit —
  re-equip must restore them; verify and report.
- **`<skill.var.enchant-level>` inside metaskills**: any console error
  naming the variable invalidates the pattern — report immediately.
- **`entitytype` / `world` / `triggerblocktype` gates**: wrong mobs
  triggering, wrong world applying, or ore lines never firing all point
  at the gate — quote the console line.
- **Potion-type names** in this pack beyond the previously proven
  RESISTANCE/SPEED/REGEN (e.g. BLINDNESS, HUNGER, INVISIBILITY,
  WATER_BREATHING, FAST_DIGGING, INCREASE_DAMAGE): a load error on
  `potion{type=...}` means that name needs checking against the wiki.
