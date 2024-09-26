import pandas as pd

# Criando o objeto Series
dados = pd.Series([4, 7, 8, -2], index=['a', 'b', 'c', 'd'])

# Calculando e imprimindo a média da Series
media = dados.mean()
print(f'Média da Series: {media}')

# Multiplicando os valores por 2 e imprimindo
multiplicado = dados * 2
print('Valores multiplicados por 2:')
print(multiplicado)

# Selecionando e imprimindo o valor no índice 'a'
valor_a = dados['a']
print(f'Valor no índice "a": {valor_a}')
valor_b = dados['b']
print(f'Valor no índice "b": {valor_b}')
valor_c = dados['c']
print(f'Valor no índice "c": {valor_c}')
valor_d = dados['d']
print(f'Valor no índice "d": {valor_d}')