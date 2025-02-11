import os
import sqlite3
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from tkinter import Tk, Button, Label, messagebox
from threading import Thread
from generate_excel import generate_student_data, write_to_excel
from generate_db import excel_to_sql
from sync import synchronize_files

# Funzione per generare utenti
def genera_utenti():
    try:
        num_students = 10
        headers = ["NOME", "COGNOME", "DATA DI NASCITA", "LUOGO DI NASCITA", "CODICE FISCALE", "EMAIL", "CONTATTO TELEFONICO", "RESIDENZA\\INDIRIZZO"]
        student_data = generate_student_data(num_students)
        write_to_excel(excel_file, headers, student_data)
        messagebox.showinfo("Genera Utenti", "Il file Excel è stato generato correttamente!")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante la generazione degli utenti: {e}")

# Funzione per esportare in SQL
def esporta_in_sql():
    try:
        excel_to_sql(excel_file, db_file)
        messagebox.showinfo("Esporta in SQL", "Il database è stato creato correttamente dai dati Excel!")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante l'esportazione in SQL: {e}")

# Funzione per sincronizzare i file
def start_sync():
    try:
        synchronize_files(excel_file, db_file)
        messagebox.showinfo("Sincronizza", "La sincronizzazione è stata completata correttamente!")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante la sincronizzazione: {e}")

# Funzione per uscire dal programma
def exit_program():
    root.quit()

# Parametri del file
# Ottiene il percorso della directory corrente
current_directory = os.path.dirname(__file__)

# Percorsi dei file dinamici
excel_file = os.path.join(current_directory, 'utenti.xlsx')
db_file = os.path.join(current_directory, 'database.db')

# Configurazione GUI
root = Tk()
root.title("Sincronizzazione Dati")
root.geometry("300x250")

label = Label(root, text="Premi il pulsante per eseguire l'azione desiderata")
label.pack(pady=20)

button_generate = Button(root, text="Genera Utenti", command=genera_utenti)
button_generate.pack(pady=10)

button_export = Button(root, text="Esporta in SQL", command=esporta_in_sql)
button_export.pack(pady=10)

button_sync = Button(root, text="Sincronizza", command=start_sync)
button_sync.pack(pady=10)

button_exit = Button(root, text="Esci", command=exit_program)
button_exit.pack(pady=10)

root.mainloop()
