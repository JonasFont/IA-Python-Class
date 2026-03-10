import pandas as pd
import requests
from io import StringIO

# URL do Google Sheets (CSV)
google_sheets_url = "https://docs.google.com/spreadsheets/d/1XPng6Xxq_eNkfW4ASEgaXdHoZml6UxVmTkjygXeGfFk/export?format=csv"

# Baixar o arquivo CSV
response = requests.get(google_sheets_url)
csv_data = response.content.decode('utf-8')

# Ler o CSV usando pandas
df = pd.read_csv(StringIO(csv_data))

# Opções disponíveis para análise
options = {
    '0': 'Para sair do programa',
    '1': 'Quantidade de infectados por um determinado estado',
    '2': 'Quantos se vacinaram naquele determinado estado',
    '3': 'Mortes por estado'
}

# Mostrar opções ao usuário
print("Escolha uma opção para análise:")
for key, value in options.items():
    print(f"{key}. {value}")

# Solicitar ao usuário para escolher uma opção
selected_option = input("\nDigite o número da opção desejada (1, 2 ou 3): ").strip()

# Função para analisar a opção escolhida pelo usuário
def analyze_option(option):
    if option == '0':
        print(f"Obrigado por usar o sistema")
        exit()

    elif option == '1':
        state = input("\nDigite a sigla do estado (exemplo: SP para São Paulo): ").strip().upper()
        if state in df['state'].unique():
            infected = df[df['state'] == state]['totalCases'].iloc[-1]
            print(f"\nQuantidade de infectados em {state}: {infected} casos")
        else:
            print(f"Não há dados disponíveis para o estado {state}.")
    elif option == '2':
        state = input("\nDigite a sigla do estado (exemplo: SP para São Paulo): ").strip().upper()
        if state in df['state'].unique():
            vaccinated = df[df['state'] == state]['vaccinated'].iloc[-1]
            print(f"\nNúmero de pessoas vacinadas em {state}: {vaccinated}")
        else:
            print(f"Não há dados disponíveis para o estado {state}.")
    elif option == '3':
        state = input("\nDigite a sigla do estado (exemplo: SP para São Paulo): ").strip().upper()
        if state in df['state'].unique():
            deaths = df[df['state'] == state]['deaths'].iloc[-1]
            print(f"\nNúmero de mortes em {state}: {deaths}")
        else:
            print(f"Não há dados disponíveis para o estado {state}.")
    else:
        print("Opção inválida.")

while True:

    # Executar a análise conforme a opção selecionada pelo usuário
    if selected_option in options.keys():
        analyze_option(selected_option)
    else:
        print("Opção inválida. Por favor, selecione uma opção válida (0 , 1, 2 ou 3).")

