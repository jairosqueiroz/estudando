while True:
    try:
        salario = float(input("Digite o salário do colaborador: R$ "))
        break
    except ValueError:
        print("Por favor, digite um valor válido.")

percentuais = {
    (1500, float('inf')): 5,
    (700, 1500): 10,
    (280, 700): 15,
    (0, 280): 20
}

for faixa, percentual in percentuais.items():
    if faixa[0] <= salario < faixa[1]:
        aumento = (salario * percentual / 100)
        novo_salario = salario + aumento
        print(f"Salário atual: R$ {salario:.2f}")
        print(f"Percentual de aumento aplicado: {percentual}%")
        print(f"Valor do aumento: R$ {aumento:.2f} ")
        print(f"Novo salário: R$ {novo_salario:.2f}")
        break
