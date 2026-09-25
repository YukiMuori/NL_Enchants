[English](README.md) · **Italiano**

# NL_Enchants

**Incantesimi personalizzati vanilla-friendly di Neverland** per MythicEnchants +
MythicMobs. Un pacchetto di incantesimi di produzione per il server **Neverland
Survival**: effetti contestuali, meccaniche reattive e brevi, VFX leggibili —
ogni incantesimo spiegabile in una frase.

- **Namespace:** `nl` (es. `nl:double_jump`)
- **Lingue:** Inglese (`en_us`) e Italiano (`it_it`)
- **Licenza:** MIT
- **Catalogo:** 30 incantesimi in 8 categorie

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
├── vfx/
│   └── <categoria>/<id>.yml      solo presentazione (metaskill NL_VFX_*)
├── datapack/nl/                  frammenti datapack con namespace nl (tag)
├── resourcepack/                 asset client: voci di lingua en_us / it_it
├── docs/
│   ├── enchantments/<id>.md      una scheda tecnica per incantesimo
│   ├── development.md · balancing.md · compatibility.md · localization.md
├── tools/validate.py             validazione statica (YAML, ID, riferimenti, lingue)
└── README.md · README.it.md · SETUP.md · CHANGELOG.md · LICENSE
```

## Catalogo incantesimi

Ogni voce ha una scheda completa in [`docs/enchantments/`](docs/enchantments/)
(effetto, trigger, VFX, note di bilanciamento, valutazione prestazioni,
limiti noti). Gruppi di oggetti: arma = spade+asce, armatura = qualsiasi pezzo,
stivali, arco, piccone, zappa, attrezzi.

### Combattimento · `enchantments/combat/`

| ID | Nome | Rarità | Max | Oggetti | Effetto |
| --- | --- | --- | --- | --- | --- |
| `nl:sluggish` | Sbavato | UNCOMMON | III | arma | I tuoi colpi possono intrappolare il bersaglio in una nebbia vischiosa. |
| `nl:bleeding` | Sanguinante | UNCOMMON | III | arma | I tuoi colpi possono aprire ferite che continuano a sanguinare. |
| `nl:staggering` | Barcollante | RARE | II | arma | I tuoi colpi possono far perdere l'equilibrio al bersaglio per un istante. |
| `nl:executioner` | Esecutore | RARE | III | arma | I colpi contro bersagli indeboliti colpiscono più forte — e vedi quando sono vulnerabili. |
| `nl:predator` | Predatore | RARE | II | arma | Contrattacca con più forza il nemico che ti ha appena colpito. |
| `nl:momentum` | Impeto | UNCOMMON | III | arma | Le uccisioni in serie ti tengono rapido — subire un colpo spezza la catena. |
| `nl:echo` | Eco | EPIC | III | arma | Una parte del tuo colpo a volte si ripete un istante dopo. |
| `nl:mark` | Marchio | RARE | I | arma | Il primo colpo marchia il bersaglio — i colpi successivi sul marchiato colpiscono più forte. |

### Distanza · `enchantments/ranged/`

| ID | Nome | Rarità | Max | Oggetti | Effetto |
| --- | --- | --- | --- | --- | --- |
| `nl:hawkeye` | Occhio di Falco | RARE | II | arco | I colpi ad arco completamente teso volano più forti e più veri. |
| `nl:ricochet` | Rimbalzo | EPIC | I | arco | Una freccia mancata rimbalza una volta verso un nemico vicino. |
| `nl:recall` | Richiamo | UNCOMMON | I | arco | Le frecce a volte tornano nella tua faretra dopo l'impatto. |

### Movimento · `enchantments/movement/`

| ID | Nome | Rarità | Max | Oggetti | Effetto |
| --- | --- | --- | --- | --- | --- |
| `nl:double_jump` | Doppio Salto | RARE | I | stivali | Premi di nuovo il tasto di salto mentre sei in aria per eseguire un secondo balzo. |
| `nl:shadowstep` | Passo d'Ombra | RARE | I | stivali | Se colpito, puoi scivolare all'indietro lasciando dietro di te la tua ombra. |
| `nl:climber` | Scalatore | UNCOMMON | I | stivali | Corri per arrampicarti più velocemente su scale e liane; salta per slanciarti via. |

### Estrazione · `enchantments/mining/`

| ID | Nome | Rarità | Max | Oggetti | Effetto |
| --- | --- | --- | --- | --- | --- |
| `nl:shatter` | Frantuma | RARE | III | piccone | Il tuo piccone a volte frantuma i blocchi adiacenti della stessa famiglia. |
| `nl:prospector` | Prospezione | RARE | I | piccone | Estrarre minerale invia un impulso: se diamanti si nascondono nelle vicinanze, canta. |
| `nl:conservation` | Conservazione | UNCOMMON | II | attrezzi | I tuoi attrezzi a volte ignorano l'usura. |

### Agricoltura · `enchantments/farming/`

| ID | Nome | Rarità | Max | Oggetti | Effetto |
| --- | --- | --- | --- | --- | --- |
| `nl:green_thumb` | Mano Verde | COMMON | II | zappa | Raccogliere a volte sparge un'ondata di crescita intorno a te. |
| `nl:reaping` | Mietitura | RARE | I | zappa | Raccogliere a volte porta via in un colpo solo anche le colture vicine. |
| `nl:replanter` | Ripiantatore | COMMON | I | zappa | Le colture raccolte vengono immediatamente riseminate. |

### Difesa · `enchantments/defensive/`

| ID | Nome | Rarità | Max | Oggetti | Effetto |
| --- | --- | --- | --- | --- | --- |
| `nl:grounded` | Radicamento | UNCOMMON | II | armatura | Stai saldo — una parte della spinta subita scivola su di te. |
| `nl:reprisal` | Riflesso | UNCOMMON | III | armatura | I colpi subiti a volte rispondono mordendo l'attaccante. |
| `nl:second_wind` | Secondo Fiato | RARE | II | armatura | Sull'orlo della fine, uno slancio di vigore ti porta un po' più avanti. |
| `nl:tenacity` | Tenacia | RARE | II | armatura | Incassare colpo dopo colpo ti indurisce contro i successivi. |

### Esplorazione · `enchantments/exploration/`

| ID | Nome | Rarità | Max | Oggetti | Effetto |
| --- | --- | --- | --- | --- | --- |
| `nl:sentinel` | Sentinella | RARE | I | elmo | Il tuo elmo si agita silenziosamente quando occhi ostili ti osservano. |
| `nl:wayfarer` | Viandante | UNCOMMON | I | armatura | Lunghi tratti di viaggio onesto ti ricompensano con un momento di vigore. |

### Leggendari · `enchantments/legendary/`

| ID | Nome | Rarità | Max | Oggetti | Effetto |
| --- | --- | --- | --- | --- | --- |
| `nl:resonance` | Risonanza | LEGENDARY | I | armatura | I pezzi sintonizzati vibrano insieme, ricucendo lentamente le tue ferite. |
| `nl:voidbound` | Vincolato al Vuoto | MYTHIC | I | armatura | Quando la morte ti avrebbe preso, il Vuoto si rifiuta, per una volta, di raccoglierti. |
| `nl:reflection` | Riflesso Speculare | LEGENDARY | I | armatura | L'acciaio in volo si rivolta contro il suo arciere. |
| `nl:soulbond` | Anima Gemella | LEGENDARY | I | armatura | L'equipaggiamento legato rifiuta di lasciarti — e lega anche i suoi compagni. |

> **Nota sui nomi:** la lista di concept originale assegnava il nome italiano
> *Riflesso* sia a Reprisal sia a Reflection. Reprisal mantiene *Riflesso*
> (come specificato per primo); Reflection usa *Riflesso Speculare* — gli ID
> non cambiano. Vedi `docs/enchantments/reflection.md`.

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

> **Stato validazione:** *la v0.3.0 è una ricostruzione di affidabilità —
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
