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

38 incantesimi in 6 categorie, portati dalla lista "Vanilla+" di AdvancedEnchantments. Le probabilità scalano col livello se non indicato.
Le note di design di ogni incantesimo sono in `docs/enchantments/<id>.md`; i numeri completi sono in `docs/balancing.md`; cosa è stato scartato e perché è in `docs/enchantments/_skipped-from-ae-list.md`.

> Nota tooltip: in vanilla si vede solo il nome — la riga descrizione richiede il mod client "Enchantment Descriptions" (vedi SETUP.md). Questa tabella è il riferimento.

### Combat

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Gelo Artico | `nl:arctic_freeze` | 3 | UNCOMMON | 5+5%/livello: Lentezza I 3s + brivido di 1 danno/s per 3s |
| Blackout | `nl:blackout` | 5 | UNCOMMON | 4+4%/livello: Cecità 2s al colpo |
| Colpo Doppio | `nl:double_blow` | 4 | RARE | 10+5%/livello: colpo extra di danno livello+2 (tridente) |
| Drenaggio | `nl:drain` | 7 | RARE | 12%: danno livello+1 e ti cura di livello PV |
| Flagello dell'Ender | `nl:enderbane` | 5 | RARE | +1+livello danni ad Enderman, Endermite, Shulker, Drago dell'End |
| Frantumazombie | `nl:zombie_crusher` | 3 | UNCOMMON | +livello danni a zombie e varianti |
| Frantumateschi | `nl:skullcrusher` | 3 | UNCOMMON | +livello danni a scheletri e varianti |
| Incenerisci | `nl:incinerate` | 3 | UNCOMMON | +1+livello danni + fiamme ai ragni |
| Mietifuoco | `nl:blaze_reaper` | 3 | RARE | +1+livello danni alle creature del Nether |
| Cubismo | `nl:cubism` | 3 | UNCOMMON | +1+livello danni a Slime e Cubi di Magma |
| Primo Colpo | `nl:first_strike` | 3 | UNCOMMON | +1+livello danni finché il bersaglio è sopra il 95% di vita |
| Colpo di Grazia | `nl:finishing` | 3 | UNCOMMON | +1+livello danni quando il bersaglio è sotto il 30% di vita |
| Rinvio | `nl:postpone` | 3 | COMMON | 10+10%/livello: il colpo non causa knockback |
| Rinculo | `nl:repel` | 3 | COMMON | 8+8%/livello: scaglia il bersaglio in alto e all'indietro |
| Fame Nera | `nl:starvation` | 3 | COMMON | 8+8%/livello: Fame I per 5s |
| Thor | `nl:thor` | 3 | RARE | 5+5%/livello: fulmine vero che infligge livello danni (armi melee) |
| Ninja | `nl:ninja` | 3 | RARE | i colpi in sneak infliggono +1+livello danni |
| Fame da Lupo | `nl:ravenous` | 4 | UNCOMMON | 10+10%/livello: recupera livello+1 cibo e saturazione combattendo |

### Arci e Balestre

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Raffica | `nl:multi_shot` | 3 | RARE | 25%: scocca una raffica di 1+livello frecce sul bersaglio |
| Flashbang | `nl:flashbang` | 3 | UNCOMMON | 15+15%/livello: Cecità 3s al colpo |
| Gelo | `nl:frost` | 3 | UNCOMMON | 10+10%/livello: congelamento neve in polvere per 1,5s + livello×1s |
| Esplosiva | `nl:explosive` | 5 | RARE | 8+8%/livello: esplosione visiva + danno livello+1 (non rompe mai blocchi) |

### Miniera

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Estrazione a Blast | `nl:blast_mining` | 3 | RARE | 34%/livello: rompe un'area 3×3×3 (max 2+2×livello blocchi, usura attrezzo applicata) |
| Esperienza | `nl:experience` | 5 | UNCOMMON | 10+10%/livello: bottiglia d'XP extra dai minerali estratti |
| Raccolta | `nl:foraging` | 3 | COMMON | 15+15%/livello: bastone e arboscello extra dalle foglie |
| Prospezione dell'Nether | `nl:nether_prospector` | 3 | UNCOMMON | 10+10%/livello: Antico Detrito extra |
| Celerità | `nl:haste` | 3 | RARE | Celerità I mentre l'attrezzo è in mano |

### Difesa

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Adrenalina | `nl:adrenaline` | 3 | UNCOMMON | 15+15%/livello: Forza I 4s quando un mob ostile ti colpisce |
| Affinità dell'End | `nl:end_affinity` | 3 | UNCOMMON | -15%/livello danni subiti nell'End (max 50%) |
| Affinità del Nether | `nl:nether_affinity` | 3 | UNCOMMON | -15%/livello danni subiti nel Nether (max 50%) |
| Rimbalzo | `nl:rebounding` | 3 | RARE | danno melee subito -10%/livello (max 30%), ne riflette il 20%/livello |
| Scuotimento | `nl:rumble` | 3 | UNCOMMON | 10+10%/livello: danno livello+1 a tutti i mob entro 3 blocchi quando colpito |
| Ardente | `nl:scorching` | 3 | COMMON | 15%: incendiato l'attaccante per 1s + livello×1s |
| Svanire | `nl:vanish` | 3 | UNCOMMON | 4+4%/livello (attesa 10s): Invisibilità 3s dopo un colpo subito |
| Acquatica | `nl:waterborne` | 1 | UNCOMMON | Apnea mentre l'elmo è indossato |

### Movimento

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Fuga | `nl:escape` | 2 | COMMON | 30% (attesa 8s): Velocità I 3s dopo un colpo subito |
| Passo di Piuma | `nl:feather_step` | 5 | RARE | 20+16%/livello: annulla completamente i danni da caduta |

### Agricoltura

| Incantesimo | ID | Max | Rarità | Cosa fa |
| --- | --- | --- | --- | --- |
| Risema | `nl:replenish` | 1 | COMMON | i raccolti maturi si riseminano istantaneamente; quelli giovani non vengono toccati |

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
