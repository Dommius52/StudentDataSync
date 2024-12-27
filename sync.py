import pandas as pd
import sqlite3
import os
import time
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

# Funzione per leggere i dati dal file Excel e inserirli nella tabella SQL
def excel_to_sql(excel_file, db_file):
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        print(f"Errore: Il file {excel_file} non è stato trovato.")
        return
    except Exception as e:
        print(f"Errore durante la lettura del file Excel: {e}")
        return

    try:
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
    except sqlite3.Error as e:
        print(f"Errore durante l'interazione con il database SQLite: {e}")
    finally:
        if conn:
            conn.close()

# Funzione per leggere i dati dalla tabella SQL e salvarli nel file Excel
def sql_to_excel(db_file, excel_file):
    try:
        conn = sqlite3.connect(db_file)
        df = pd.read_sql_query('SELECT * FROM utenti', conn)

        # Salva i dati nel file Excel
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Utenti')
            ws = writer.sheets['Utenti']

            # Regola la larghezza delle colonne in base ai dati
            for col in ws.iter_cols():
                max_length = 0
                column = get_column_letter(col[0].column)
                for cell in col:
                    try:
                        if cell.value:
                            if len(str(cell.value)) > max_length:
                                max_length = len(cell.value)
                    except:
                        pass
                adjusted_width = max_length + 2
                ws.column_dimensions[column].width = adjusted_width

    except sqlite3.Error as e:
        print(f"Errore durante l'interazione con il database SQLite: {e}")
    except Exception as e:
        print(f"Errore durante la scrittura del file Excel: {e}")
    finally:
        if conn:
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
