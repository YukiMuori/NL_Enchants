# datapack/nl

Server-side datapack fragments that belong to the `nl` namespace.

MythicEnchants **auto-generates and maintains** the live enchantment datapack
in each world (`<world>/datapacks/MythicEnchants/`) from the files in
`enchantments/` — this folder does **not** replace it.

This folder is the home for optional, hand-authored datapack content that
belongs to the pack, following the Mythic Pack convention:

```
plugins/MythicMobs/packs/NL_Enchants/datapack/nl/...
```

At the moment it contains no data. Expected future use:

- `datapack/nl/tags/enchantment/...` — enchantment tags (e.g. custom
  exclusivity or loot groups referenced by `Tags:`/`ConflictingEnchants:`)
- `datapack/nl/tags/item/...` — custom item tags if a future enchant needs a
  `SupportedItems` group that vanilla does not provide

Per the MythicEnchants pack documentation, tags created for packs must live
under the pack's namespace directory so they resolve as `nl:<tag>`.
