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
