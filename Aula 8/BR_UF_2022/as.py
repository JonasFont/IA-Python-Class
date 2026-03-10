import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Carregar os dados de COVID-19
file_path = 'cases-brazil-total.csv'
data = pd.read_csv(file_path)

# Carregar o shapefile dos estados brasileiros
shapefile_base = 'BR_Malha_Preliminar_Distrito_2022'
extensions = ['.shp', '.shx', '.dbf', '.prj', '.cpg']

for ext in extensions:
    if not os.path.exists(shapefile_base + ext):
        raise FileNotFoundError(f"O arquivo {shapefile_base + ext} não foi encontrado.")

# Carregar o shapefile dos estados brasileiros
states_geo = gpd.read_file(shapefile_base + '.shp')

# Inspecionar os primeiros registros dos dados
print("Primeiros registros dos dados de COVID-19:")
print(data.head())

print("\nPrimeiros registros dos dados geoespaciais:")
print(states_geo.head())

# Ajustar os nomes dos estados nos dados de COVID-19 para combinar com os nomes no shapefile
data['state'] = data['state'].str.upper()

# Verificar os valores únicos nas colunas de união
print("\nValores únicos na coluna 'state' dos dados de COVID-19:")
print(data['state'].unique())

print("\nValores únicos na coluna 'NM_UF' dos dados geoespaciais:")
print(states_geo['NM_UF'].unique())

# Unir os dados de COVID-19 com os dados geoespaciais
merged = states_geo.set_index('NM_UF').join(data.set_index('state'))

# Verificar as colunas do DataFrame resultante da junção
print("\nColunas do DataFrame unido:")
print(merged.columns)

# Inspecionar os primeiros registros dos dados unidos
print("\nPrimeiros registros dos dados unidos:")
print(merged.head())

# Verificar se as colunas 'vaccinated' e 'vaccinated_second' estão presentes
if 'vaccinated' not in merged.columns or 'vaccinated_second' not in merged.columns:
    raise KeyError("Colunas 'vaccinated' ou 'vaccinated_second' não encontradas nos dados unidos.")

# Plotar a incidência de vacinados
fig, ax = plt.subplots(1, 2, figsize=(20, 10))

# Mapa de fundo do Brasil
states_geo.plot(ax=ax[0], color='white', edgecolor='black')
# Adicionar dados de COVID-19 ao mapa de fundo
merged.plot(column='vaccinated', cmap='OrRd', linewidth=0.8, ax=ax[0], legend=True)
ax[0].set_title('Brasileiros vacinados com a primeira dose')

# Mapa de fundo do Brasil
states_geo.plot(ax=ax[1], color='white', edgecolor='black')
# Adicionar dados de COVID-19 ao mapa de fundo
merged.plot(column='vaccinated_second', cmap='OrRd', linewidth=0.8, ax=ax[1], legend=True)
ax[1].set_title('Brasileiros vacinados com a Segunda dose')

plt.show()
