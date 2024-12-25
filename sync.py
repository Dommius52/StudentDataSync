import pandas as pd
import sqlite3
import os
import time

# Funzione per leggere i dati dal file Excel e inserirli nella tabella SQL
def excel_to_sql(excel_file, db_file):
    df = pd.read_excel(excel_file)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        nome TEXT,
        cognome TEXT,
        data_di_nascita TEXT,
        luogo_di_nascita TEXT,
        codice_fiscale TEXT,
        email TEXT,
        contatto_telefonico TEXT,
        indirizzo_residenza TEXT
    )
    ''')

    cursor.execute('DELETE FROM utenti')

    for row in df.itertuples(index=False):
        cursor.execute('''
        INSERT INTO utenti (nome, cognome, data_di_nascita, luogo_di_nascita, codice_fiscale, email, contatto_telefonico, indirizzo_residenza)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

    conn.commit()
    conn.close()

# Funzione per leggere i dati dalla tabella SQL e salvarli nel file Excel
def sql_to_excel(db_file, excel_file):
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query('SELECT * FROM utenti', conn)

    df.to_excel(excel_file, index=False)

    conn.close()

# Funzione per sincronizzare i dati tra Excel e SQL
def synchronize_files(excel_file, db_file):
    last_excel_mod_time = os.path.getmtime(excel_file)
    last_db_mod_time = os.path.getmtime(db_file)

    while True:
        current_excel_mod_time = os.path.getmtime(excel_file)
        current_db_mod_time = os.path.getmtime(db_file)

        if current_excel_mod_time != last_excel_mod_time:
            excel_to_sql(excel_file, db_file)
            last_excel_mod_time = current_excel_mod_time
            print("Database aggiornato dai dati Excel.")

        if current_db_mod_time != last_db_mod_time:
            sql_to_excel(db_file, excel_file)
            last_db_mod_time = current_db_mod_time
            print("File Excel aggiornato dai dati del database.")

        time.sleep(1)  # Controlla le modifiche ogni secondo

# Parametri del file
excel_file = 'C:/Users/39329/OneDrive/Desktop/UNIPEGASO/visualcode/StudentDataSync/utenti.xlsx'
db_file = 'C:/Users/39329/OneDrive/Desktop/UNIPEGASO/visualcode/StudentDataSync/database.db'

# Sincronizza i dati inizialmente
excel_to_sql(excel_file, db_file)
sql_to_excel(db_file, excel_file)

# Avvia la sincronizzazione continua
synchronize_files(excel_file, db_file)
