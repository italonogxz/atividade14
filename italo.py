# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Digite o valor do seu salário: R$"))
if salario <= 1250:
    aumento1 = (salario * 10) / 100
    print("O seu aumento de 10% é igual a: R$", aumento1)
    salariofinal1 = salario + aumento1
    print("O seu salário agora é: R$", salariofinal1)
elif salario > 1250:
    aumento2 = (salario * 15) / 100
    print("O seu aumento de 15% é igual a: R$", aumento2)
    salariofinal2 = salario + aumento2
    print("O seu salário agora é: R$", salariofinal2)
    