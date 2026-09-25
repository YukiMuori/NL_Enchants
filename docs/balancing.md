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

## Current tuning — 0.1.0

### nl:double_jump

| Parameter | Value | Rationale |
| --- | --- | --- |
| Impulse | `+0.42 Y` (velocity ADD) | identical to a vanilla jump — reads as a native mechanic |
| Charge window | 100 ticks (5 s) | generous to react, too short to bank for ledge saves |
| Settle delay | 3 ticks | prevents boosting during ground-jump startup frames |
| Internal input guard | 1 s | absorbs key-repeat spam; invisible to normal play |
| MaxLevel | 1 | binary ability, nothing to scale |
| Enchanting | Weight 4, MinCost 18, MaxCost 42 | RARE band, mid-tier table cost |
| AnvilCost | 6 | meaningful but not punishing |

PvP stance: the double jump is predictable (fixed delay, fixed impulse) and
therefore counterable; it was deliberately not built as an escape tool
(no horizontal dash, no slow-falling component).
