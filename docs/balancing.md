# Balancing Notes

## Philosophy

NL_Enchants is a **vanilla-friendly Survival** pack. Numbers are chosen so a
player can understand an enchantment from one sentence and feel it working
without it dominating the game.

- Short, contextual, reactive effects over permanent stat inflation.
- Every level must be a meaningful step; binary mechanics stay at MaxLevel 1.
- Rarity describes identity (utility → signature), enchanting-table
  `Weight`/`MinCost`/`MaxCost` control actual availability (MythicEnchants
  decouples the two).
- No instant kills, no screen clutter, no passive particle noise.

## Tuning levers per enchantment

| Lever | Where |
| --- | --- |
| Chance / duration / magnitude | skill lines in `skills/<category>/` |
| Availability | `Enchanting:` block (Weight, MinCost, MaxCost) |
| Exclusivity | `ConflictingEnchants:`, `Tags:` |
| Presentation | `vfx/<category>/` — never balance through VFX |

## Balance change policy

Any gameplay-value change is a release note. Balance tweaks bump the PATCH
version and are listed in `CHANGELOG.md` with the old and new value. VFX-only
changes are also PATCH entries, clearly marked as cosmetic.

## Current tuning — 0.2.0

Availability bands by rarity (Weight / MinCost / MaxCost / AnvilCost):

| Rarity | Weight | MinCost | MaxCost | AnvilCost |
| --- | --- | --- | --- | --- |
| COMMON | 6 | 4 | 24 | 1 |
| UNCOMMON | 5 | 8 | 30 | 2 |
| RARE | 3 | 16 | 38 | 4 |
| EPIC | 2 | 24 | 44 | 5 |
| LEGENDARY | 1–2 | 30 | 50 | 7 |
| MYTHIC | 1 | 35 | 55 | 8 |

### Per-enchant tuning

| Enchant | Key values |
| --- | --- |
| `nl:double_jump` | impulse +0.42 Y · charge 5s · settle 3t · MaxLevel I |
| `nl:sluggish` | chance 12/16/20% · Slow 2.5s (amp by level) |
| `nl:bleeding` | chance 12% · 1 dmg/s · 3/4/5s |
| `nl:staggering` | chance 10/14% · root ~0.3s · conflicts sluggish |
| `nl:executioner` | threshold <30% HP · +1/+2/+3 dmg · marker 3s cd |
| `nl:predator` | stalk 5s · +2/+3 dmg · consumed on use |
| `nl:momentum` | stacks max 5 · 5s · Speed I–III · broken by damage |
| `nl:echo` | 25% · delay 0.3s · 10/20/30% of item_attack · cd 2s |
| `nl:mark` | mark 8s · +1.5 dmg on marked · refresh on hit · MaxLevel I |
| `nl:hawkeye` | focus 2s (braced draw) · release tension >0.9 · +1.5/+3 arrow dmg |
| `nl:ricochet` | window 4s · nearest hostile ≤10b · 4 flat dmg · 1 bounce |
| `nl:recall` | miss 35% / hit 20% · 1 arrow · cd 2s |
| `nl:shadowstep` | 25% on damaged · backward hop · cd 5s · MaxLevel I |
| `nl:climber` | sprint climb +0.1 Y/tick · jump leap +0.42 Y · climbables only |
| `nl:shatter` | stone 15/20/25% max 12 · ore 12/16/20% max 8 · 3×3×3 · perblock=2 |
| `nl:prospector` | 3-tier ping · valuable ores · r=8 · cd 6s |
| `nl:conservation` | negate 25/35% per durability point |
| `nl:green_thumb` | chance 15/20% · crop-only · single block |
| `nl:reaping` | 35% · 3×3×3 max 8 crops · perblock=2 |
| `nl:replanter` | instant replant · MaxLevel I · QoL |
| `nl:grounded` | +20%/+40% KB resistance per piece (stacks across pieces) |
| `nl:reprisal` | 20% · 2/3/4 thorns dmg · conflicts reflection |
| `nl:second_wind` | trigger <30% HP · Regen I 3/4s + Speed I 3s · cd 45s |
| `nl:tenacity` | window 5s · Resistance I 2/3s while chain lives |
| `nl:sentinel` | scan / 5s · r=12 · max 4 marked · chime-only |
| `nl:wayfarer` | moving+outdoor+grounded · Regen II 3s · cd 60s |
| `nl:resonance` | Regen I 2s → II 8s by exact piece count · pulse / 8s |
| `nl:voidbound` | lethal negate (totem-aware) + Absorption II 10s · cd 600s |
| `nl:reflection` | projectile hits halved, half returned · cd 8s · MaxLevel I |
| `nl:soulbond` | per-item 3 death charges · 2+ pieces bind whole outfit |

PvP stance: the double jump is predictable (fixed delay, fixed impulse) and
therefore counterable; it was deliberately not built as an escape tool
(no horizontal dash, no slow-falling component).

General PvP stance for the full catalog: every combat/defensive reaction is
either chance-gated, cooldown-gated, or consume-on-use; no enchant multiplies
weapon damage beyond +4 flat in its best case (executioner III); no movement
enchant grants sustained speed (momentum's Speed expires with the kill
chain); emergency saves (voidbound, second_wind) are mutually exclusive by
conflict and on long internal cooldowns.
