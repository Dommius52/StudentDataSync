# Project Work

## IT

### Descrizione
Progetto conclusivo Terzo anno, facoltà di informatica L-31 Unipegaso. L'obiettivo è creare un sistema per generare dati casuali, nel mio caso di studenti dell'Ateneo, di età tra i 18 e i 35 anni e trasferirli in un file Excel e un database SQL.

### Il progetto è composto da:
1. **Generazione di Dati e Creazione di File Excel**: Usa la libreria Faker per generare dati casuali e li salva in un file Excel.
2. **Sincronizzazione dei Dati tra Excel e SQLite**: Sincronizza i dati tra un file Excel e un database SQLite.

### Struttura del Progetto
- `generate_excel.py`: Script per generare dati casuali degli studenti e salvarli in un file Excel.
- `generate_db.py`: Script per creare la tabella SQL e inserire i dati dal file Excel in un database SQLite.
- `sync.py`: Script per sincronizzare i dati tra il file Excel e il database SQLite.
- `GUI_Test.py`: Interfaccia grafica per generare utenti, esportare in SQL e sincronizzare i file.

### Come Eseguire il Progetto

#### Prerequisiti
Assicurarsi di avere installato i seguenti pacchetti per l'utilizzo delle librerie:
- `faker`
- `openpyxl`
- `pandas`

Puoi installarli usando pip:
```sh
pip install faker openpyxl pandas
```

### Esecuzione
1. **Generare i Dati degli Studenti**:
   Esegui `generate_excel.py` per creare un file Excel con i dati degli studenti.
   ```sh
   python generate_excel.py
   ```

2. **Esportare in SQL**:
   Esegui `generate_db.py` per creare la tabella SQL e inserire i dati dal file Excel.
   ```sh
   python generate_db.py
   ```

3. **Sincronizzare i Dati**:
   Esegui `sync.py` per avviare la sincronizzazione dei dati tra il file Excel e il database SQLite.
   ```sh
   python sync.py
   ```

4. **Utilizzare la GUI**:
   Esegui `GUI_Test.py` per utilizzare l'interfaccia grafica per generare utenti, esportare in SQL e sincronizzare i file.
   ```sh
   python GUI_Test.py
   ```

### Funzionamento del Codice

#### generate_excel.py
- Usa la libreria Faker per generare dati come nome, cognome, data di nascita, luogo di nascita, codice fiscale, email, contatto telefonico e indirizzo di residenza.
- Salva questi dati in un file Excel utilizzando openpyxl.

#### generate_db.py
- Legge i dati dal file Excel e li inserisce in una tabella SQL.

#### sync.py
- Sincronizza i dati tra il file Excel e il database SQLite.

#### GUI_Test.py
- Interfaccia grafica per eseguire le azioni sopra descritte tramite pulsanti.

### Possibili Miglioramenti
- Aggiungere la validazione dei dati per garantire l'integrità dei dati inseriti nel database.
- Implementare ulteriori funzionalità nella GUI per semplificare l'interazione con il sistema.

### Autore
Questo progetto è stato sviluppato da Domenico Emilio Ietto.

---

## EN

### Description
Final project for the third year, Computer Science faculty L-31 Unipegaso. The objective is to create a system to generate random data, in my case, of University students, aged between 18 and 35, and transfer it to an Excel file and an SQL database.

### The project consists of:
1. **Data Generation and Excel File Creation**: Uses the Faker library to generate random data and saves it to an Excel file.
2. **Data Synchronization between Excel and SQLite**: Synchronizes data between an Excel file and an SQLite database.

### Project Structure
- `generate_excel.py`: Script to generate random student data and save it to an Excel file.
- `generate_db.py`: Script to create the SQL table and insert data from the Excel file into an SQLite database.
- `sync.py`: Script to synchronize data between the Excel file and the SQLite database.
- `GUI_Test.py`: Graphical interface to generate users, export to SQL, and synchronize files.

### How to Run the Project

#### Prerequisites
Make sure to have the following packages installed:
- `faker`
- `openpyxl`
- `pandas`

You can install them using pip:
```sh
pip install faker openpyxl pandas
```

### Execution
1. **Generate Student Data**:
   Run `generate_excel.py` to create an Excel file with student data.
   ```sh
   python generate_excel.py
   ```

2. **Export to SQL**:
   Run `generate_db.py` to create the SQL table and insert data from the Excel file.
   ```sh
   python generate_db.py
   ```

3. **Synchronize Data**:
   Run `sync.py` to start data synchronization between the Excel file and the SQLite database.
   ```sh
   python sync.py
   ```

4. **Use the GUI**:
   Run `GUI_Test.py` to use the graphical interface to generate users, export to SQL, and synchronize files.
   ```sh
   python GUI_Test.py
   ```

### Code Functionality

#### generate_excel.py
- Uses the Faker library to generate data such as name, surname, date of birth, place of birth, tax code, email, phone contact, and residence address.
- Saves this data in an Excel file using openpyxl.

#### generate_db.py
- Reads data from the Excel file and inserts it into an SQL table.

#### sync.py
- Synchronizes data between the Excel file and the SQLite database.

#### GUI_Test.py
- Graphical interface to perform the actions described above through buttons.

### Possible Improvements
- Add data validation to ensure the integrity of data entered into the database.
- Implement additional features in the GUI to simplify interaction with the system.

### Author
This project was developed by Domenico Emilio Ietto.


