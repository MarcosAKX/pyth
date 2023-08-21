
#Menu de opções
menu = int(input('Escolha uma das opções do menu: 1- Novo salário, 2- Férias, 3-Décimo Terceiro , 4- sair.'))


if menu == 1:
    salario = float(input('Digite seu salário atual:'))
    if salario <= 350:
        aumento = (salario * 15) / 100
        print('Seu novo salário é:', salario + aumento )
    elif salario  >= 350 and salario <= 600:
        aumento2 = (salario *10) / 100
        print('Seu novo salário é:', salario + aumento2)
    elif salario > 600:
        aumento3 = (salario *5) / 100
        print('Seu novo salário é:', salario + aumento3)
elif menu == 2:
    salario = float(input('Digite seu salário atual:'))
    ferias = salario / 2
    print('Você receberá de férias:', salario + ferias)
elif menu == 3:
    salario = float(input('Digite seu salário atual:'))
    meses = int(input('Digite seu tempo na empresa em meses (máximo 12 meses):'))
    decimo = (salario * meses) / 12
    print('Seu décimo terceiro será:', decimo)
elif menu == 4:
    exit
