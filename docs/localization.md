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
enchantment.nl.<id>.desc   description (tooltip-description convention)
```

**Verified fact (field + docs, 0.5.0):** vanilla Minecraft shows ONLY the
enchantment name in item tooltips. A description line under the name does
not exist in vanilla — it is provided by client-side mods, which share one
key convention:

- **Enchantment Descriptions** (Darkhax) reads `enchantment.<ns>.<path>.desc`
  — exactly our keys; our `nl:` descriptions work out of the box.
- **Item Tooltips** reads `enchantment.<ns>.<path>.description`, falling back
  to `.desc` — our keys also match via the fallback.

For vanilla clients no datapack/resource pack can add the description line;
the player-facing reference is the README catalog tables (name, ID, max
level, rarity, effect — both languages).

The live translation key resolution depends on what MythicEnchants' generated
datapack emits (literal text vs. `translate` components). Runtime
verification step:

1. Install the pack and the merged resource pack.
2. Set the client language to Italian.
3. Look at an item enchanted with `nl:thor`.
4. If the name shows "Thor" it proves nothing about the layer used — check
   the generated datapack directly: open
   `world/datapacks/MythicEnchants/data/nl/enchantment/thor.json` and look
   at the `description` field. `{"translate": "enchantment.nl.thor"}` → the
   datapack resolves translate keys and the resource pack controls names.
   A baked literal string → the generator uses server-side strings and the
   resource pack only serves mod clients. Update this file with the
   observed behavior.
5. With the "Enchantment Descriptions" client mod installed, the description
   line must appear under the name (Italian client → Italian text).

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
