from faker import Faker
import pandas as pd
import random

# Configurar a biblioteca Faker
fake = Faker()

def generate_real_estate_data(n):
    # Tipos de propriedades fictícias para o dataset
    property_types = ["Casa", "Apartamento", "Terreno", "Loft", "Chácara", "Condomínio"]

    # Gerar dados fictícios
    property_ids = [i+1 for i in range(n)]
    addresses = [fake.address().replace("\n", ", ") for _ in range(n)]
    types = [fake.random_element(elements=property_types) for _ in range(n)]
    bedrooms = [fake.random_int(min=1, max=6) for _ in range(n)]
    bathrooms = [fake.random_int(min=1, max=4) for _ in range(n)]
    area = [fake.random_int(min=40, max=500) for _ in range(n)]
    prices = [round(random.uniform(50000, 2000000), 2) for _ in range(n)]
    construction_dates = [fake.date_between_dates(date_start=pd.to_datetime("1990-01-01"), date_end=pd.to_datetime("2023-01-01")) for _ in range(n)]
    garage = [fake.random_element(elements=["Sim", "Não"]) for _ in range(n)]
    descriptions = [fake.sentence(nb_words=10) for _ in range(n)]

    # Criar DataFrame
    data = {
        "ID da Propriedade": property_ids,
        "Endereço": addresses,
        "Tipo": types,
        "Quartos": bedrooms,
        "Banheiros": bathrooms,
        "Área (m²)": area,
        "Preço ($)": prices,
        "Data de Construção": construction_dates,
        "Garagem": garage,
        "Descrição": descriptions
    }
    return pd.DataFrame(data)

# Gere um dataset com 100 linhas de dados fictícios
df = generate_real_estate_data(100)
print(df)
