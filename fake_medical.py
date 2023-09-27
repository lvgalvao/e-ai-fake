from faker import Faker
import pandas as pd
import random

# Configurar a biblioteca Faker
fake = Faker()

def generate_medical_data(n):
    # Alergias, medicações e tipos sanguíneos fictícios para o dataset
    allergies = ["Penicilina", "Polén", "Látex", "Amendoim", "Glúten", "Nenhum"]
    medications = ["Atorvastatina", "Lisinopril", "Metformina", "Sertralina", "Nenhum"]
    blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

    # Gerar dados fictícios
    patient_ids = [i+1 for i in range(n)]
    patient_names = [fake.name() for _ in range(n)]
    birth_dates = [fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=100) for _ in range(n)]
    blood_types_data = [fake.random_element(elements=blood_types) for _ in range(n)]
    heights = [fake.random_int(min=140, max=210) for _ in range(n)]
    weights = [round(random.uniform(40.0, 120.0), 1) for _ in range(n)]
    patient_allergies = [fake.random_element(elements=allergies) for _ in range(n)]
    regular_medications = [fake.random_element(elements=medications) for _ in range(n)]
    last_appointment = [fake.date_this_year(before_today=True, after_today=False) for _ in range(n)]
    diagnosis = [fake.sentence(nb_words=5) for _ in range(n)]

    # Criar DataFrame
    data = {
        "ID do Paciente": patient_ids,
        "Nome": patient_names,
        "Data de Nascimento": birth_dates,
        "Tipo Sanguíneo": blood_types_data,
        "Altura (cm)": heights,
        "Peso (kg)": weights,
        "Alergias": patient_allergies,
        "Medicação Regular": regular_medications,
        "Última Consulta": last_appointment,
        "Diagnóstico": diagnosis
    }
    return pd.DataFrame(data)

# Gere um dataset com 100 linhas de dados fictícios
df = generate_medical_data(100)

# Salve o dataset em um arquivo CSV
df.to_csv('fake_medical.csv', index=False)

print(df)
