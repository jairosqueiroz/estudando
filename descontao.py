salario = input("Digite o salário do colaborador: R$ ")
salario = float(salario)

if salario > 1500 :
    percentual = 5
elif salario > 700 :
    percentual = 10
elif salario > 280 :
    percentual = 15
else :
    percentual = 20

aumento = (salario * percentual / 100)
novo_salario = salario + aumento

print(f"Salário atual: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")  # Removed the % sign
