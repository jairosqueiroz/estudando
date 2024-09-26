import pandas as pd

# Criação da base fictícia em CSV
data = {
    'ID': [1, 2, 3, 4],
    'DATA': ['01/01/2019', '10/02/2019', '30/05/2019', '29/06/2019'],
    'PRODUTO': ['TOALHA', 'SABONETE', 'MOUSE', 'TECLADO'],
    'QNT': [6, 5, 3, 2],
    'VALOR UNIDADE': ['R$ 35,00', 'R$ 3,00', 'R$ 10,00', 'R$ 38,00'],
    'TOTAL': ['R$ 210,00', 'R$ 15,00', 'R$ 30,00', 'R$ 76,00'],
    'SETOR': ['MesaBanho', 'Perfumaria', 'Informática', 'Informática']
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Salvando o DataFrame em um arquivo CSV
df.to_csv('baseficticia.csv', sep=';', index=False)

# Leitura do arquivo CSV
df = pd.read_csv('baseficticia.csv', sep=';')

# Impressão dos setores
print(df['SETOR'])

# Impressão da quantidade de compras por setor
print(df['SETOR'].value_counts())
