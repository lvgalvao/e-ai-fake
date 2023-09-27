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
