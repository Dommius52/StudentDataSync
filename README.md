###Project Work###

## Descrizione

Progetto conclusivo Terzo anno, facoltà di informatica L-31 Unipegaso. 
L'obiettivo è creare un sistema per generare dati casuali, nel mio caso di studenti dell'Ateneo, di età tra i 18 e i 35 anni e trasferireli in un file Excel e un database SQL. 

Il progetto è composto da due script principali:

1. **Generazione di Dati e Creazione di File Excel**: Usa la libreria `Faker` per generare dati casuali e li salva in un file Excel.
2. **Sincronizzazione dei Dati tra Excel e SQLite**: Sincronizza i dati tra un file Excel e un database SQLite in tempo reale.

## Struttura del Progetto

- `generate_data.py`: Script per generare dati casuali degli studenti e salvarli in un file Excel.
- `sync_data.py`: Script per creare tabella SQL e sincronizzare i dati tra il file Excel e un database SQLite.

## Come Eseguire il Progetto

### Prerequisiti

Assicurati di avere installato i seguenti pacchetti:

- `faker`
- `openpyxl`
- `pandas`

Puoi installarli usando pip:
```bash
pip install faker openpyxl pandas
```


### Esecuzione

1. **Generare i Dati degli Studenti**:
   Esegui `generate_data.py` per creare un file Excel con i dati degli studenti.
   ```bash
   python generate_data.py
   ```

2. **Sincronizzare i Dati**:
   Esegui `sync_data.py` per avviare la sincronizzazione dei dati tra il file Excel e il database SQLite.
   ```bash
   python sync_data.py
   ```

## Funzionamento del Codice

### `generate_data.py`

- Usa la libreria `Faker` per generare dati come nome, cognome, data di nascita, luogo di nascita, codice fiscale, email, contatto telefonico e indirizzo di residenza.
- Salva questi dati in un file Excel utilizzando `openpyxl`.

### `sync_data.py`

- Legge i dati dal file Excel e li inserisce in una tabella SQL.
- Sincronizza continuamente i dati tra il file Excel e il database SQLite verificando le modifiche ogni secondo.

### Possibili Miglioramenti ###

- Aggiungere la validazione dei dati per garantire l'integrità dei dati inseriti nel database.
- Aggiungere funzioni che gestiscano le eccezioni, come blocco `try`
- Implementare una GUI per semplificare l'interazione con il sistema di sincronizzazione.


## Autore

Questo progetto è stato sviluppato da [Domenico Emilio Ietto]
