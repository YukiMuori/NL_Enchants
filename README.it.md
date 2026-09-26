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

> Tooltip: vanilla Minecraft mostra solo il nome — per la riga descrizione serve il mod client "Enchantment Descriptions" (vedi SETUP.md).

### Combat

| Incantesimo | ID | Max | Rarità | Effetto |
| --- | --- | --- | --- | --- |
| Gelo Artico | `nl:arctic_freeze` | 3 | UNCOMMON | Possibilità di gelare il bersaglio fino alle ossa. |
| Blackout | `nl:blackout` | 5 | UNCOMMON | Acceca l'avversario. |
| Colpo Doppio | `nl:double_blow` | 4 | RARE | Possibilità di colpire due volte col tridente. |
| Drenaggio | `nl:drain` | 7 | RARE | Drena il tuo avversario, nutrendoti. |
| Flagello dell'Ender | `nl:enderbane` | 5 | RARE | Aumenta i danni alle creature dell'End. |
| Frantumazombie | `nl:zombie_crusher` | 3 | UNCOMMON | Aumenta i danni inflitti agli zombie. |
| Frantumateschi | `nl:skullcrusher` | 3 | UNCOMMON | Aumenta i danni inflitti agli scheletri. |
| Incenerisci | `nl:incinerate` | 3 | UNCOMMON | Aumenta i danni inflitti ai ragni. |
| Mietifuoco | `nl:blaze_reaper` | 3 | RARE | Aumenta i danni alle creature del Nether. |
| Cubismo | `nl:cubism` | 3 | UNCOMMON | Più danni a Slime e Cubi di Magma. |
| Primo Colpo | `nl:first_strike` | 3 | UNCOMMON | Più danni ai nemici a vita piena. |
| Colpo di Grazia | `nl:finishing` | 3 | UNCOMMON | Aumenta i danni ai nemici a bassa vita. |
| Rinvio | `nl:postpone` | 3 | COMMON | Possibilità di non causare knockback al bersaglio. |
| Rinculo | `nl:repel` | 3 | COMMON | Possibilità di scagliare indietro l'avversario. |
| Fame Nera | `nl:starvation` | 3 | COMMON | Possibilità di infliggere fame all'avversario. |
| Thor | `nl:thor` | 3 | RARE | Possibilità di fulminare l'avversario. |
| Ninja | `nl:ninja` | 3 | RARE | Più danni colpendo furtivamente. |
| Fame da Lupo | `nl:ravenous` | 4 | UNCOMMON | Possibilità di recuperare fame combattendo. |

### Arci e Balestre

| Incantesimo | ID | Max | Rarità | Effetto |
| --- | --- | --- | --- | --- |
| Raffica | `nl:multi_shot` | 3 | RARE | Fa piovere frecce sul tuo avversario. |
| Flashbang | `nl:flashbang` | 3 | UNCOMMON | Acceca l'avversario al colpo. |
| Gelo | `nl:frost` | 3 | UNCOMMON | Possibilità di congelare l'avversario. |
| Esplosiva | `nl:explosive` | 5 | RARE | Possibilità che le frecce esplodano. |

### Miniera

| Incantesimo | ID | Max | Rarità | Effetto |
| --- | --- | --- | --- | --- |
| Estrazione a Blast | `nl:blast_mining` | 3 | RARE | Estrae i blocchi in un'area 3x3. |
| Esperienza | `nl:experience` | 5 | UNCOMMON | Possibilità di ottenere più esperienza dai minerali. |
| Raccolta | `nl:foraging` | 3 | COMMON | Possibilità di moltiplicare il bottino delle foglie. |
| Prospezione dell'Nether | `nl:nether_prospector` | 3 | UNCOMMON | Possibilità di moltiplicare l'Antico Detrito. |
| Celerità | `nl:haste` | 3 | RARE | Usa i tuoi attrezzi più velocemente. |

### Difesa

| Incantesimo | ID | Max | Rarità | Effetto |
| --- | --- | --- | --- | --- |
| Adrenalina | `nl:adrenaline` | 3 | UNCOMMON | Ottieni Forza difendendoti dagli attacchi dei mob. |
| Affinità dell'End | `nl:end_affinity` | 3 | UNCOMMON | Riduce i danni subiti nell'End. |
| Affinità del Nether | `nl:nether_affinity` | 3 | UNCOMMON | Riduce i danni subiti nel Nether. |
| Rimbalzo | `nl:rebounding` | 3 | RARE | Rimanda il danno melee all'attaccante. |
| Scuotimento | `nl:rumble` | 3 | UNCOMMON | Contrattacca le entità intorno a te quando colpito. |
| Ardente | `nl:scorching` | 3 | COMMON | Possibilità di incendiare chi ti attacca. |
| Svanire | `nl:vanish` | 3 | UNCOMMON | Sparisci per 3 secondi dopo aver subito un colpo. |
| Acquatica | `nl:waterborne` | 1 | UNCOMMON | Respira sott'acqua. |

### Movimento

| Incantesimo | ID | Max | Rarità | Effetto |
| --- | --- | --- | --- | --- |
| Fuga | `nl:escape` | 2 | COMMON | Uno scatto di velocità dopo aver subito un danno. |
| Passo di Piuma | `nl:feather_step` | 5 | RARE | Possibilità di annullare i danni da caduta. |

### Agricoltura

| Incantesimo | ID | Max | Rarità | Effetto |
| --- | --- | --- | --- | --- |
| Risema | `nl:replenish` | 1 | COMMON | Risema le colture quando le rompi. |

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
