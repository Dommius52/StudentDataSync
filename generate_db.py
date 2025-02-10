import pandas as pd
import sqlite3

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
        print(f"Il database '{db_file}' è stato aggiornato correttamente dai dati Excel!")
    except sqlite3.Error as e:
        print(f"Errore durante l'interazione con il database SQLite: {e}")
    finally:
        if conn:
            conn.close()

# Esegui la generazione del database
if __name__ == "__main__":
    excel_file = 'C:/Users/39329/OneDrive/Desktop/UNIPEGASO/visualcode/StudentDataSync/utenti.xlsx'
    db_file = 'C:/Users/39329/OneDrive/Desktop/UNIPEGASO/visualcode/StudentDataSync/database.db'
    excel_to_sql(excel_file, db_file)
