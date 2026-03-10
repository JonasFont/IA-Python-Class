import pandas as pd
import matplotlib.pyplot as plt

# Criar um DataFrame
data = {'Ano': [2010, 2011, 2012, 2013, 2014],
        'Vendas': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

# Plotar o DataFrame
df.plot(x='Ano', y='Vendas', kind='line')
plt.title('Vendas ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.show()
