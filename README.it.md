[English](README.md) · **Italiano**

# NL_Enchants

**Incantesimi personalizzati vanilla-friendly di Neverland** per MythicEnchants +
MythicMobs. Un pacchetto di incantesimi di produzione per il server **Neverland
Survival**: effetti contestuali, meccaniche reattive e brevi, VFX leggibili —
ogni incantesimo spiegabile in una frase.

- **Namespace:** `nl` (es. `nl:swift_strike`)
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

14 incantesimi dalla lista utility vanilla+ richiesta (meccaniche verificate — vedi `docs/catalog-plan.md`; 4 scarti con motivazione in `docs/enchantments/_skipped-from-list.md`).

> Nota tooltip: in vanilla si vede solo il nome — la riga descrizione richiede il mod client "Enchantment Descriptions" (vedi SETUP.md). Questa tabella è il riferimento.

### Combat

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Aspetto Glaciale | `nl:ice_aspect` | 2 | RARE | 10%/livello: congela la vittima per 3s (può comunque guardarsi intorno e difendersi) |
| Ragnatela | `nl:websnare` | 2 | UNCOMMON | 8+8%/livello: una ragnatela compare sotto la vittima, intrappolandola |
| Colpo Rapido | `nl:swift_strike` | 5 | UNCOMMON | +0.6 velocità d'attacco/livello — fino al 75% di recupero più rapido al liv. 5 |
| Portata Ampia | `nl:outreach` | 2 | RARE | +0.5/livello di portata d'attacco — fino a 4 blocchi al liv. 2 |

### Archi

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Tossico | `nl:toxic` | 1 | UNCOMMON | le frecce avvelenano la vittima 11s; i non-morti sono immuni. Solo arco |
| Soffio della Brezza | `nl:breeze_burst` | 1 | RARE | le frecce scatenano una raffica all'impatto e rilasciano una Carica di Vento |

### Attrezzi

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Tocco del Granchio | `nl:crabs_touch` | 3 | RARE | +1/livello di portata sui blocchi (7,5 al liv. 3); funziona anche nella seconda mano — rompe e piazza da lontano |

### Difesa

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Vitalità | `nl:vitality` | 3 | RARE | +2 vita massima/livello — 13 cuori al liv. 3 mentre indossata |
| Guardia del Cielo | `nl:skyguard` | 4 | RARE | solo elytra: −4%/livello danni subiti (la Protezione delle elytra) |
| Protezione Cinetica | `nl:kinetic_protection` | 4 | UNCOMMON | −25%/livello danni cinetici dell'elytra (schianto contro i muri) |
| Recupero | `nl:retrieval` | 4 | UNCOMMON | 20%/livello: le frecce che ti colpiscono vengono recuperate nel tuo inventario (80% al liv. 4) |
| Graviole | `nl:graviole` | 3 | RARE | solo elytra: gravità −10%/livello — voli più lunghi e plananti, velocità massima ridotta |

### Movimento

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Passo Ardente | `nl:scorch_walker` | 2 | RARE | cammina sulla lava su blocchi di magma; immune a magma e neve in polvere; al liv. 2 anche alla lava |
| Passo Lungo | `nl:stride` | 3 | UNCOMMON | salga i blocchi interi senza saltare (gradini più alti a liv. 2/3) |

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
