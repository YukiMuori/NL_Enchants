# Localization

NL_Enchants supports **English (`en_us`)** and **Italian (`it_it`)**.

## Two layers

### 1. Server-side strings (`enchantments/*.yml`)

`Display` and `Description` in the enchantment YAML are the canonical
server-side strings (English). MythicEnchants shows them on items, in
placeholders and rich-text contexts. They are the source of truth for the
datapack; they are **not** per-player translatable.

### 2. Client-side strings (`resourcepack/`)

`resourcepack/assets/minecraft/lang/{en_us,it_it}.json` provide the standard
vanilla translation keys for every enchantment:

```text
enchantment.nl.<id>        display name
enchantment.nl.<id>.desc   description (vanilla 1.21 tooltip description key)
```

The live translation key resolution depends on what MythicEnchants' generated
datapack emits (literal text vs. `translate` components). Runtime
verification step:

1. Install the pack and the merged resource pack.
2. Set the client language to Italian.
3. Look at an item enchanted with `nl:double_jump`.
4. If the name shows "Doppio Salto" → the datapack resolves translate keys
   and everything works. If it shows "Double Jump" → the generator bakes
   server-side strings, and the resource pack then only serves future/other
   keys; update this file with the observed behavior.

Keep both layers synchronized whenever an enchant is added or renamed: the
validator (`tools/validate.py`) checks that every `nl:` enchant has both
language entries in both files.

The player-facing catalog is documented in both languages: `README.md`
(English) and `README.it.md` (Italiano) — the Italian catalog table quotes
exactly the `it_it.json` description strings.

## Rules

- Technical IDs (`nl:double_jump`) are language-independent and frozen.
- Italian names never become IDs.
- Descriptions are localized in both languages, always.
