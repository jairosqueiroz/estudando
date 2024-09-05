nota1 = input("Primeira nota parcial: ")

nota2 = input("Segunda nota parcial: ")

media = (float(nota1) + float(nota2)) / 2

if media >= 9 :

conceito = "A"

elif media >= 7.5 :

conceito = "B"

elif media >= 6 :

conceito = "C"

elif media >= 4 :

conceito = "D"

else :

conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C" :

resultado = "APROVADO"

else :

resultado = "REPROVADO"

print(f"Nota 1: {nota1}")

print(f"Nota 2: {nota2}")

print(f"Média: {media}")

print(f"Conceito: {conceito}")

print(f"Resultado: {resultado}")
