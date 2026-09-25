# Changelog

All notable changes to NL_Enchants are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/) · Versioning:
[SemVer](https://semver.org/) — MAJOR breaking · MINOR enchant/feature ·
PATCH fix/balance. Gameplay values are never changed silently.

## [0.3.0] — 2026-09-26

**Reliability rebuild.** Field testing showed most of the 0.2.0 catalog
non-functional. Root cause: bare `<math:enchant_level>` variables inside
metaskills (documented only for direct enchant lines) → unresolvable →
metaskill aborted. Every enchant was rebuilt on patterns proven by official
documentation, and the reliability rules are now enforced pack-wide
(`docs/development.md`).

### Fixed (architecture)

- All metaskills now use `<skill.var.enchant-level>`; direct enchant lines
  use `<math:...>`; aura-tick/delayed skills use constants only (R1).
- Dispatch lines aligned to official trigger/target semantics:
  `~onAttack → @target`, `~onDamaged → @self`/`@trigger`, `~onBlockBreak →
  @self`/`@origin` (R2); metaskill mechanics inherit targets (R3).
- One condition per line — comma lists removed from all conditions;
  material lists live only in mechanics that document them (veinminer) (R4).
- `CancelIfNoTargets: false` on utility metaskills without guaranteed
  targets (R5).

### Redesigned (unverified mechanisms removed)

- `nl:hawkeye` → direct `arrowbuff` on `~onShoot` gated by inline
  `bowtension{value=>0.9}` (official patterns only; draw-focus listeners
  removed). New description.
- `nl:green_thumb` → growth burst (bonemeal) on harvest; hoe-`~onUse`
  design removed. New description.
- `nl:prospector` → "Diamond Sense": strong/soft presence ping via
  `blocktypeinradius` (single-material conditions).
- `nl:sentinel` → self-centered pulse (per-mob marking used an unverified
  targeter).
- `nl:resonance` → two tiers (any piece / full set) with plain conditions.
- `nl:soulbond` → outfit binding now requires the full set (plain
  conditions instead of composite chains).
- `nl:shatter` / `nl:reaping` → one single-tag gate line per block family;
  lists only inside veinminer.
- `nl:echo` / `nl:momentum` / `nl:tenacity` / `nl:second_wind` → fixed
  values instead of level math in fragile contexts.
- `nl:voidbound` / `nl:reflection` → flat `reducedamage` amounts
  (`a=1000` + cap) — no damage variable inside metaskills.

### Added

- `docs/testing.md` — full in-game test protocol (per-enchant matrix,
  architecture checks, known-risk list).
- Reliability rules section in `docs/development.md`.

### Validation status

- Static validation: **completed**.
- Runtime validation: **REQUIRED — this is the release that must be
  field-tested before any enchant is considered working.**

## [0.2.1] — 2026-09-25

Documentation and localization release — no gameplay changes.

### Added

- **Italian README** (`README.it.md`): full translation, including the
  complete 30-enchantment catalog with Italian names and the exact
  descriptions shipped in the `it_it` lang file. Language switcher banner
  on both READMEs.
- `packinfo.yml` description is now bilingual (EN + IT) for the
  `/mm menu` pack hover.

### Changed

- **Italian localization pass** — polished 9 `it_it` description strings
  for natural phrasing (removed anglicisms, punctuation consistency):
  executioner, mark, momentum, prospector, reaping, replanter, grounded,
  second_wind, voidbound. Cosmetic only; display names and IDs untouched.

## [0.2.0] — 2026-09-25

Full catalog release: all 30 enchantments of the Neverland concept list,
with the repository reorganized to one file per enchantment.

### Changed

- **Layout refactor**: every enchantment now lives in its own file —
  `enchantments/<category>/<id>.yml` (file name = enchant ID), with matching
  `skills/<category>/<id>.yml` and `vfx/<category>/<id>.yml`. The validator
  enforces the layout.

### Added — combat (8)
`nl:sluggish` (Sbavato/Sluggish), `nl:bleeding` (Sanguinante/Bleeding),
`nl:staggering` (Barcollante/Staggering), `nl:executioner`
(Esecutore/Executioner), `nl:predator` (Predatore/Predator), `nl:momentum`
(Impeto/Momentum), `nl:echo` (Eco/Echo), `nl:mark` (Marchio/Mark).

### Added — ranged (3)
`nl:hawkeye` (Occhio di Falco/Hawkeye), `nl:ricochet` (Rimbalzo/Ricochet),
`nl:recall` (Richiamo/Recall).

### Added — movement (2)
`nl:shadowstep` (Passo d'Ombra/Shadowstep), `nl:climber` (Scalatore/Climber).

### Added — mining (3)
`nl:shatter` (Frantuma/Shatter), `nl:prospector` (Prospezione/Prospector),
`nl:conservation` (Conservazione/Conservation).

### Added — farming (3)
`nl:green_thumb` (Mano Verde/Green Thumb), `nl:reaping` (Mietitura/Reaping),
`nl:replanter` (Ripiantatore/Replanter).

### Added — defensive (4)
`nl:grounded` (Radicamento/Grounded), `nl:reprisal` (Riflesso/Reprisal),
`nl:second_wind` (Secondo Fiato/Second Wind), `nl:tenacity` (Tenacia/Tenacity).

### Added — exploration (2)
`nl:sentinel` (Sentinella/Sentinel), `nl:wayfarer` (Viandante/Wayfarer —
designed from the intentionally-underspecified master concept: continuous
outdoor travel is rewarded with periodic vigor).

### Added — legendary (4)
`nl:resonance` (Risonanza/Resonance — piece-count set synergy via
`hasMythicEnchant` slot conditions), `nl:voidbound` (Vincolato al
Vuoto/Voidbound — lethal-hit negation, 10 min cooldown, MYTHIC),
`nl:reflection` (Riflesso Speculare/Reflection — projectile half-reflect),
`nl:soulbond` (Anima Gemella/Soulbond — death protection via `recoveritem`,
outfit binding at 2+ pieces).

### Design decisions

- **Naming collision resolved**: the concept list assigned *Riflesso* to
  both Reprisal and Reflection. Reprisal keeps *Riflesso*; Reflection uses
  *Riflesso Speculare*. IDs unaffected.
- **Prospector** reveals ore *presence and intensity* (3-tier ping) instead
  of exact positions — per-block reveal requires Premium inline targeter
  conditions, deliberately out of scope.
- **Reaping** may break immature neighbor crops at 35% (they drop only
  seeds) — crop age checks are unavailable in the free syntax set;
  documented in its spec. Pairs with `nl:replanter`.
- **Conflict groups**: sluggish↔staggering (control), second_wind↔voidbound
  (emergency), reprisal↔reflection (defensive reaction).

## [0.1.0] — 2026-09-25

Initial public scaffold of the pack: repository architecture, pack
metadata, localization layer, and the reference implementation enchantment.

### Added

- **Repository structure & metadata**: `packinfo.yml` (MythicMobs pack
  metadata, `FileDependencies` on MythicEnchants), `SETUP.md`, `README.md`,
  `LICENSE` (MIT), `.gitignore`, `datapack/nl/` namespace placeholder,
  layered `enchantments/ · skills/ · vfx/` architecture per category.
- **Enchantment `nl:double_jump` ("Double Jump" / "Doppio Salto")** —
  movement, RARE, MaxLevel I, boots (`#minecraft:enchantable/foot_armor`).
  After jumping, pressing the jump key again while airborne performs a
  second, vanilla-strength leap; driven by a 5-second self-expiring charge
  granted on every ground jump. Full specification:
  `docs/enchantments/double_jump.md`.
- **Skills**: `skills/movement/double_jump.yml` — equip/unequip listener
  auras (Paper `onJump` + `OnInput` components), charge arming, guarded
  second-jump impulse.
- **VFX**: activation-only cloud/end-rod burst + layered airy audio (22
  particles, 2 sounds per activation).
- **Localization**: `resourcepack/` with `en_us` and `it_it` enchantment
  name + description entries and `pack.mcmeta`; localization policy in
  `docs/localization.md`.
- **Documentation**: `docs/development.md` (architecture, conventions,
  verified-syntax policy, checklist), `docs/balancing.md`,
  `docs/compatibility.md` (Paper-only features, Geyser caveat, edge cases).
- **Tooling**: `tools/validate.py` — static validation of YAML, enchant ID
  namespace/rules, required fields, skill-ID uniqueness, `skill{s=}`
  reference resolution, localization completeness, per-enchant docs.

### Validation status

- Static validation: **completed** (see `tools/validate.py`).
- Runtime validation on Paper + MythicMobs + MythicEnchants:
  **required** — not yet performed.

[0.2.1]: https://github.com/YukiMuori/NL_Enchants/releases/tag/v0.2.1
[0.2.0]: https://github.com/YukiMuori/NL_Enchants/releases/tag/v0.2.0
[0.1.0]: https://github.com/YukiMuori/NL_Enchants/releases/tag/v0.1.0
