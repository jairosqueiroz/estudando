# 1) Importe a biblioteca Pandas
import pandas as pd

# 2) Importe o Matplotlib
import matplotlib.pyplot as plt

# 3) Crie um conjunto de dados fictícios
dados = {
    'X': [1, 2, 3, 4, 5, 6],
    'Y1': [120, 110, 130, 145, 118, 125],
    'Y2': [95, 54, 86, 77, 90, 81]
}

# 4) Crie um dataframe a partir destes dados
df = pd.DataFrame(dados)

# 5) Crie o código para “plotar” estes valores e imprima o resultado
plt.plot(df['X'], df['Y1'], label='Y1')
plt.plot(df['X'], df['Y2'], label='Y2')
plt.xlabel('X')
plt.ylabel('Valores')
plt.title('Gráfico de Y1 e Y2 em função de X')
plt.legend()
plt.show()
