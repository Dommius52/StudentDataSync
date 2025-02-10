import os
import sqlite3
import pandas as pd
from openpyxl.utils import get_column_letter
from generate_db import excel_to_sql

def sql_to_excel(db_file, excel_file):
    try:
        conn = sqlite3.connect(db_file)
        df = pd.read_sql_query('SELECT * FROM utenti', conn)

        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Utenti')
            ws = writer.sheets['Utenti']

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

        print("File Excel aggiornato")
    except sqlite3.Error as e:
        print(f"Errore durante l'interazione con il database SQLite: {e}")
    except Exception as e:
        print(f"Errore durante la scrittura del file Excel: {e}")
    finally:
        if conn:
            conn.close()

def synchronize_files(excel_file, db_file, force_sync=False):
    try:
        if not os.path.exists(db_file):
            excel_to_sql(excel_file, db_file)
            print(f"Database '{db_file}' creato e aggiornato dai dati Excel.")
        
        last_excel_mod_time = os.path.getmtime(excel_file)
        last_db_mod_time = os.path.getmtime(db_file)

        current_excel_mod_time = os.path.getmtime(excel_file)
        current_db_mod_time = os.path.getmtime(db_file)

        if force_sync or current_excel_mod_time != last_excel_mod_time:
            excel_to_sql(excel_file, db_file)
            last_excel_mod_time = current_excel_mod_time
            print("Database aggiornato dai dati Excel.")
        else:
            print("Nessuna modifica è stata apportata al file Excel.")

        if force_sync or current_db_mod_time != last_db_mod_time:
            sql_to_excel(db_file, excel_file)
            last_db_mod_time = current_db_mod_time
            print("File Excel aggiornato dai dati del database.")
        else:
            print("Nessuna modifica è stata apportata al file SQL.")
    except Exception as e:
        print(f"Errore durante la sincronizzazione: {e}")

if __name__ == "__main__":
    excel_file = 'C:/Users/39329/OneDrive/Desktop/UNIPEGASO/visualcode/StudentDataSync/utenti.xlsx'
    db_file = 'C:/Users/39329/OneDrive/Desktop/UNIPEGASO/visualcode/StudentDataSync/database.db'
    synchronize_files(excel_file, db_file, force_sync=True)

