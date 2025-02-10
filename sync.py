import os
import sqlite3
import pandas as pd
from openpyxl.utils import get_column_letter
from generate_db import excel_to_sql
import time

# Funzione per esportare i dati dal database SQLite a un file Excel
def sql_to_excel(db_file, excel_file):
    try:
        # Connessione al database SQLite
        conn = sqlite3.connect(db_file)
        # Esecuzione della query SQL per ottenere tutti i dati dalla tabella 'utenti'
        df = pd.read_sql_query('SELECT * FROM utenti', conn)

        # Scrittura dei dati su un file Excel utilizzando openpyxl
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
                                max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = max_length + 2
                ws.column_dimensions[column].width = adjusted_width

        print("File Excel aggiornato")
    except sqlite3.Error as e:
        # Gestione degli errori di interazione con il database SQLite
        print(f"Errore durante l'interazione con il database SQLite: {e}")
    except Exception as e:
        # Gestione degli errori durante la scrittura del file Excel
        print(f"Errore durante la scrittura del file Excel: {e}")
    finally:
        # Chiusura della connessione al database SQLite
        if conn:
            conn.close()

# Funzione per sincronizzare i file Excel e il database SQLite
def synchronize_files(excel_file, db_file, force_sync=False):
    try:
        # Se il database non esiste, viene creato dai dati nel file Excel
        if not os.path.exists(db_file):
            excel_to_sql(excel_file, db_file)
            print(f"Database '{db_file}' creato e aggiornato dai dati Excel.")

        last_excel_mod_time = os.path.getmtime(excel_file)
        last_db_mod_time = os.path.getmtime(db_file)

        while True:  # Loop per monitorare le modifiche ai file
            current_excel_mod_time = os.path.getmtime(excel_file)
            current_db_mod_time = os.path.getmtime(db_file)

            # Se il file Excel è stato modificato, aggiorna il database
            if current_excel_mod_time != last_excel_mod_time:
                excel_to_sql(excel_file, db_file)
                last_excel_mod_time = current_excel_mod_time
                print("Database aggiornato dai dati Excel.")

            # Se il database è stato modificato, aggiorna il file Excel
            if current_db_mod_time != last_db_mod_time:
                sql_to_excel(db_file, excel_file)
                last_db_mod_time = current_db_mod_time
                print("File Excel aggiornato dai dati del database.")

            time.sleep(1)  # Controlla le modifiche ogni secondo

    except Exception as e:
        # Gestione degli errori durante la sincronizzazione
        print(f"Errore durante la sincronizzazione: {e}")
