[English](README.md) · **Italiano**

# NL_Enchants

**Incantesimi personalizzati vanilla-friendly di Neverland** per MythicEnchants +
MythicMobs. Un pacchetto di incantesimi di produzione per il server **Neverland
Survival**: effetti contestuali, meccaniche reattive e brevi, VFX leggibili —
ogni incantesimo spiegabile in una frase.

- **Namespace:** `nl` (es. `nl:thor`)
- **Lingue:** Inglese (`en_us`) e Italiano (`it_it`)
- **Licenza:** MIT
- **Catalogo:** 38 incantesimi in 6 categorie
- **Stato:** v0.5.0 — catalogo Vanilla+ (portato dalla lista Vanilla+ di AdvancedEnchantments); test runtime sul server in arrivo (Balzo Alato, Passo d'Ombra, Emorragia, Combo, Spaccaterra, Fioritura, Ripiantatore, Sentinella); le Fasi 2–4 seguono dopo i test in gioco

> Questo README è la traduzione italiana. I nomi e le descrizioni mostrati qui
> coincidono con le stringhe del resource pack (`it_it`). Gli ID tecnici sono
> indipendenti dalla lingua e non cambiano mai.

## Requisiti

| Componente | Versione |
| --- | --- |
| Server Paper | 1.21.11+ |
| Java | 25 |
| MythicMobs | 5.12.0+ |
| MythicEnchants | versione attuale |

> MythicEnchants richiede Paper — anche questo pacchetto quindi (alcuni hook di
> runtime sono funzionalità MythicMobs esclusive di Paper). Nessun altro plugin
> è richiesto; nessuna funzionalità premium viene usata.

## Installazione

1. Copia questo repository (o un archivio di release) in
   `plugins/MythicMobs/packs/NL_Enchants/`.
2. Riavvia il server **due volte** (il primo avvio genera il datapack, il
   secondo registra gli incantesimi — requisito data-driven di MythicEnchants).
3. Unisci la cartella `resourcepack/` al resource pack del server (solo voci di
   lingua — vedi `SETUP.md`).
4. Verifica in gioco: `/enchant @s nl:double_jump 1` su un paio di stivali.

Istruzioni complete e risoluzione problemi: [SETUP.md](SETUP.md).

## Struttura delle cartelle

```text
NL_Enchants/
├── packinfo.yml                  metadati del pack (MythicMobs)
├── enchantments/
│   └── <categoria>/<id>.yml      UN FILE PER INCANTESIMO (nome file = ID)
├── skills/
│   └── <categoria>/<id>.yml      logica di gioco (metaskill NL_ENCHANT_*)
├── skills/vfx/                   solo presentazione (metaskill NL_VFX_*)
├── datapack/nl/                  frammenti datapack con namespace nl (tag)
├── resourcepack/                 asset client: voci di lingua en_us / it_it
├── docs/
│   ├── enchantments/<id>.md      una scheda tecnica per incantesimo
│   ├── development.md · balancing.md · compatibility.md · localization.md
├── tools/validate.py             validazione statica (YAML, ID, riferimenti, lingue)
└── README.md · README.it.md · SETUP.md · CHANGELOG.md · LICENSE
```

## Catalogo incantesimi

38 incantesimi in 6 categorie, portati dalla lista "Vanilla+" di AdvancedEnchantments.
Le note di design di ogni incantesimo sono in `docs/enchantments/<id>.md`; cosa è stato scartato e perché è in `docs/enchantments/_skipped-from-ae-list.md`.
### Combat

| Incantesimo | ID | Max | Rarità |
| --- | --- | --- | --- |
| Gelo Artico | `nl:arctic_freeze` | 3 | UNCOMMON |
| Blackout | `nl:blackout` | 5 | UNCOMMON |
| Colpo Doppio | `nl:double_blow` | 4 | RARE |
| Drenaggio | `nl:drain` | 7 | RARE |
| Flagello dell'Ender | `nl:enderbane` | 5 | RARE |
| Frantumazombie | `nl:zombie_crusher` | 3 | UNCOMMON |
| Frantumateschi | `nl:skullcrusher` | 3 | UNCOMMON |
| Incenerisci | `nl:incinerate` | 3 | UNCOMMON |
| Mietifuoco | `nl:blaze_reaper` | 3 | RARE |
| Cubismo | `nl:cubism` | 3 | UNCOMMON |
| Primo Colpo | `nl:first_strike` | 3 | UNCOMMON |
| Colpo di Grazia | `nl:finishing` | 3 | UNCOMMON |
| Rinvio | `nl:postpone` | 3 | COMMON |
| Rinculo | `nl:repel` | 3 | COMMON |
| Fame Nera | `nl:starvation` | 3 | COMMON |
| Thor | `nl:thor` | 3 | RARE |
| Ninja | `nl:ninja` | 3 | RARE |
| Fame da Lupo | `nl:ravenous` | 4 | UNCOMMON |### Ranged

| Incantesimo | ID | Max | Rarità |
| --- | --- | --- | --- |
| Raffica | `nl:multi_shot` | 3 | RARE |
| Flashbang | `nl:flashbang` | 3 | UNCOMMON |
| Gelo | `nl:frost` | 3 | UNCOMMON |
| Esplosiva | `nl:explosive` | 5 | RARE |### Mining

| Incantesimo | ID | Max | Rarità |
| --- | --- | --- | --- |
| Estrazione a Blast | `nl:blast_mining` | 3 | RARE |
| Esperienza | `nl:experience` | 5 | UNCOMMON |
| Raccolta | `nl:foraging` | 3 | COMMON |
| Prospezione dell'Nether | `nl:nether_prospector` | 3 | UNCOMMON |
| Celerità | `nl:haste` | 3 | RARE |### Defensive

| Incantesimo | ID | Max | Rarità |
| --- | --- | --- | --- |
| Adrenalina | `nl:adrenaline` | 3 | UNCOMMON |
| Affinità dell'End | `nl:end_affinity` | 3 | UNCOMMON |
| Affinità del Nether | `nl:nether_affinity` | 3 | UNCOMMON |
| Rimbalzo | `nl:rebounding` | 3 | RARE |
| Scuotimento | `nl:rumble` | 3 | UNCOMMON |
| Ardente | `nl:scorching` | 3 | COMMON |
| Svanire | `nl:vanish` | 3 | UNCOMMON |
| Acquatica | `nl:waterborne` | 1 | UNCOMMON |### Movement

| Incantesimo | ID | Max | Rarità |
| --- | --- | --- | --- |
| Fuga | `nl:escape` | 2 | COMMON |
| Passo di Piuma | `nl:feather_step` | 5 | RARE |### Farming

| Incantesimo | ID | Max | Rarità |
| --- | --- | --- | --- |
| Risema | `nl:replenish` | 1 | COMMON |
## Rarità

La rarità descrive l'identità e il raggruppamento di un incantesimo; la
disponibilità al tavolo d'incantamento è controllata separatamente da peso e
costo di ogni incantesimo (MythicEnchants separa deliberatamente i due aspetti).

```text
COMMON (5) · UNCOMMON (9) · RARE (12) · EPIC (2) · LEGENDARY (3) · MYTHIC (1)
```

La distribuzione segue una piramide: l'utilità semplice sta in basso, le
meccaniche distintive stanno su LEGENDARY/MYTHIC.

## Lingue

Tutti i nomi e le descrizioni degli incantesimi sono forniti in inglese e
italiano (`resourcepack/assets/minecraft/lang/`). Gli ID tecnici sono
indipendenti dalla lingua e non cambiano mai. Vedi
[docs/localization.md](docs/localization.md).

## Ricarica

- **Aggiungere o rimuovere un incantesimo** → riavvio completo del server
  (registrazione nel datapack; `/mm reload` non basta).
- **Modificare skill/VFX di un incantesimo esistente** → basta `/mm reload`
  (o `/mench reload`).

## Workflow di sviluppo

Vedi [docs/development.md](docs/development.md) per l'architettura a livelli,
la policy sulla sintassi verificata, la checklist per i nuovi incantesimi e le
convenzioni di commit. Validazione statica:

```bash
python3 tools/validate.py
```

> **Stato validazione:** *la v0.5.0 è una ricostruzione del catalogo —
> validazione statica completata; la validazione runtime su Paper +
> MythicMobs + MythicEnchants è OBBLIGATORIA.* Segui `docs/testing.md`
> (matrice di test per incantesimo) e riporta gli errori di console.
> Nulla va considerato funzionante finché non supera quel protocollo.

## Risoluzione problemi

| Sintomo | Causa probabile / soluzione |
| --- | --- |
| Gli incantesimi non compaiono dopo l'installazione | Hai riavviato una sola volta — riavvia di nuovo (caricamento in due fasi del datapack) |
| Avvisi di parse sui file incantesimi su un server senza MythicEnchants | I file vengono saltati tramite `FileDependencies`; installa MythicEnchants |
| Gli incantesimi di movimento smettono di funzionare dopo un rientro | MythicMobs elimina le aura all'uscita — rimetti gli stivali |
| Nomi degli incantesimi non tradotti in gioco | Resource pack non unito, oppure il datapack incorpora le stringhe lato server — vedi `docs/localization.md` |
| `/enchant nl:...` sconosciuto | La cartella del pack non è direttamente in `plugins/MythicMobs/packs/NL_Enchants/` |

## Contribuire

1. Segui la policy sulla sintassi — nessuna meccanica inventata; ogni riga
   non ovvia cita la sua pagina di documentazione ufficiale.
2. Un incantesimo per change set, prima la specifica, validatore verde.
3. Mantieni ID, commit e voci del changelog coerenti con
   `docs/development.md`.
