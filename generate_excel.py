from faker import Faker
import openpyxl
from openpyxl.styles import Font
import os

# Funzione per generare dati degli studenti
def generate_student_data(num_students):
    fake = Faker('it_IT')
    student_data = []
    
    for _ in range(num_students):
        nome = fake.first_name()
        cognome = fake.last_name()
        data_di_nascita = fake.date_of_birth(minimum_age=18, maximum_age=35).strftime('%d/%m/%Y')
        luogo_di_nascita = fake.city()
        codice_fiscale = fake.ssn()
        email = fake.email()
        contatto_telefonico = fake.phone_number()
        indirizzo_residenza = fake.address()
        
        student_data.append([nome, cognome, data_di_nascita, luogo_di_nascita, codice_fiscale, email, contatto_telefonico, indirizzo_residenza])
    
    return student_data

# Funzione per scrivere dati nel file Excel
def write_to_excel(file_name, headers, data):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Utenti"
    
    ws.append(headers)
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num, value=header)
        cell.font = Font(bold=True)
    
    for row in data:
        ws.append(row)
    
    # Assicurati che la directory esista
    output_directory = os.path.dirname(file_name)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Auto-regola la larghezza delle colonne
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Prende la lettera della colonna
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = max_length + 2
        ws.column_dimensions[column].width = adjusted_width

    wb.save(file_name)
    print(f"Il file Excel '{file_name}' è stato generato correttamente!")

if __name__ == "__main__":
    num_students = 10
    headers = ["NOME", "COGNOME", "DATA DI NASCITA", "LUOGO DI NASCITA", "CODICE FISCALE", "EMAIL", "CONTATTO TELEFONICO", "RESIDENZA\\INDIRIZZO"]
    student_data = generate_student_data(num_students)

    write_to_excel("C:/Users/39329/OneDrive/Desktop/UNIPEGASO/visualcode/StudentDataSync/utenti.xlsx", headers, student_data)
