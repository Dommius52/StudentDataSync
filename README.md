###Project Work###
## IT
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

Assicurarsi di avere installato i seguenti pacchetti per l'utilizzo delle librerie':

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
- Implementare una GUI per semplificare l'interazione con il sistema di sincronizzazione.


## Autore

Questo progetto è stato sviluppato da **Domenico Emilio Ietto**


### Project Work ###
## EN
## Description
Final project for the third year, Computer Science faculty L-31 Unipegaso. The objective is to create a system to generate random data, in my case, of University students, aged between 18 and 35, and transfer it to an Excel file and an SQL database.

**The project consists of two main scripts:**

1. **Data Generation and Excel File Creation**: Uses the Faker library to generate random data and saves it to an Excel file.
2. **Data Synchronization between Excel and SQLite**: Synchronizes data between an Excel file and an SQLite database in real-time.

**Project Structure**

- **generate_data.py**: Script to generate random student data and save it to an Excel file.
- **sync_data.py**: Script to create an SQL table and synchronize data between the Excel file and an SQLite database.

**How to Run the Project**

**Prerequisites**
Make sure to have the following packages installed:

- `faker`
- `openpyxl`
- `pandas`

You can install them using pip:

```bash
pip install faker openpyxl pandas
```

**Execution**

- **Generate Student Data**: Run `generate_data.py` to create an Excel file with student data.
  
```bash
python generate_data.py
```

- **Synchronize Data**: Run `sync_data.py` to start data synchronization between the Excel file and the SQLite database.

```bash
python sync_data.py
```

**Code Functionality**

- **generate_data.py**
  - Uses the Faker library to generate data such as name, surname, date of birth, place of birth, tax code, email, phone contact, and residence address.
  - Saves this data in an Excel file using openpyxl.

- **sync_data.py**
  - Reads data from the Excel file and inserts it into an SQL table.
  - Continuously synchronizes data between the Excel file and the SQLite database by checking for changes every second.

**Possible Improvements**

- Add data validation to ensure the integrity of data entered into the database.
- Implement a GUI to simplify interaction with the synchronization system.

**Author**
This project was developed by Domenico Emilio Ietto.


