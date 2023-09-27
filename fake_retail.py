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