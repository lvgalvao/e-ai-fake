# E ai Fake

Somente um projeto exemplo com alguns exemplos do uso do Faker

## Fake_medical.py

fake_medical é um pacote que gera dados médicos falsos para testes e exemplos.

```python
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
```

## Fake_real_state.py

fake_real_state é um pacote que gera dados de imóveis falsos para testes e exemplos.

```python
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
```

## Fake_user.py

fake_user é um pacote que gera dados de usuários falsos para testes e exemplos.

```python
from faker import Faker
import pandas as pd

# Configurar a biblioteca Faker para o português do Brasil
fake = Faker('pt_BR')

def generate_fake_data(n):
    data = {
        "Nome": [fake.name() for _ in range(n)],
        "Endereço": [fake.address().replace("\n", ", ") for _ in range(n)],
        "Email": [fake.email() for _ in range(n)],
        "Telefone": [fake.phone_number() for _ in range(n)],
        "Data de Nascimento": [fake.date_of_birth() for _ in range(n)],
        "Profissão": [fake.job() for _ in range(n)],
        "Empresa": [fake.company() for _ in range(n)],
        "Site": [fake.url() for _ in range(n)],
        "País": ['Brasil' for _ in range(n)]  # Como estamos usando a localização 'pt_BR', o país será fixado como Brasil.
    }
    return pd.DataFrame(data)

# Gere um dataframe com 10 linhas de dados fictícios
df = generate_fake_data(10)
df.to_csv('fake_usuario.csv', index=False)
print(df)
```

## Fake_videogame.py

fake_videogame é um pacote que gera dados de videogames falsos para testes e exemplos.

```python
from faker import Faker
import pandas as pd
import random

# Configurar a biblioteca Faker
fake = Faker()

def generate_videogame_data(n):
    # Gêneros e plataformas fictícios para o dataset
    genres = ["Ação", "Aventura", "RPG", "Esporte", "Estratégia", "Corrida", "Luta", "Simulação"]
    platforms = ["PC", "PS5", "Xbox Series X", "Switch", "Mobile"]

    # Gerar dados fictícios
    game_ids = [i+1 for i in range(n)]
    game_titles = [fake.catch_phrase() for _ in range(n)]
    game_genres = [fake.random_element(elements=genres) for _ in range(n)]
    game_platforms = [fake.random_element(elements=platforms) for _ in range(n)]
    release_years = [fake.random_int(min=2000, max=2023) for _ in range(n)]
    prices = [round(random.uniform(10.99, 199.99), 2) for _ in range(n)]
    ratings = [round(random.uniform(1, 10), 2) for _ in range(n)]
    developers = [fake.company() for _ in range(n)]
    descriptions = [fake.sentence(nb_words=10) for _ in range(n)]
    stock = [fake.random_int(min=0, max=500) for _ in range(n)]

    # Criar DataFrame
    data = {
        "ID do Game": game_ids,
        "Título": game_titles,
        "Gênero": game_genres,
        "Plataforma": game_platforms,
        "Ano de Lançamento": release_years,
        "Preço": prices,
        "Avaliação": ratings,
        "Estúdio": developers,
        "Descrição": descriptions,
        "Estoque": stock
    }
    return pd.DataFrame(data)

# Gere um dataset com 100 linhas de dados fictícios
df = generate_videogame_data(100)

# Salve o dataset em um arquivo CSV
df.to_csv('fake_videogame.csv', index=False)

print(df)
```

## Fake_retail.py

fake_retail é um pacote que gera dados de varejo falsos para testes e exemplos.

```python
from faker import Faker
import pandas as pd
import random

# Configurar a biblioteca Faker
fake = Faker()

def generate_retail_data(n):
    # Gerar dados fictícios
    sale_ids = [i+1 for i in range(n)]
    client_names = [fake.name() for _ in range(n)]
    products = [fake.bs() for _ in range(n)]  # Usando "bs()" como nome de produto genérico.
    quantities = [fake.random_int(min=1, max=10) for _ in range(n)]
    unit_prices = [round(random.uniform(1.99, 99.99), 2) for _ in range(n)]
    total_values = [quantities[i] * unit_prices[i] for i in range(n)]
    sale_dates = [fake.date_this_decade() for _ in range(n)]
    payment_methods = [fake.random_element(elements=('Cartão de Crédito', 'Boleto', 'Débito', 'Dinheiro')) for _ in range(n)]
    seller_names = [fake.first_name() for _ in range(n)]
    stores = [fake.company() for _ in range(n)]
    
    # Criar DataFrame
    data = {
        "ID da Venda": sale_ids,
        "Nome do Cliente": client_names,
        "Produto": products,
        "Quantidade": quantities,
        "Preço Unitário": unit_prices,
        "Valor Total": total_values,
        "Data da Venda": sale_dates,
        "Método de Pagamento": payment_methods,
        "Nome do Vendedor": seller_names,
        "Loja": stores
    }
    return pd.DataFrame(data)

# Gere um dataset com 100 linhas de dados fictícios
df = generate_retail_data(100)

# Salve o dataset em um arquivo CSV
df.to_csv('fake_retail.csv', index=False)
```