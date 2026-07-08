from calculos import Calculadora

cal = Calculadora()
opcao = 0

while opcao != 5:
    print("\n--- CALCULADORA POO (DESAFIO) ---")
    print("\n=== MENU ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        cal.soma(n1,n2)

    if opcao == 2:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        cal.subtracao(n1,n2)

    if opcao == 3:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        cal.multiplicacao(n1,n2)


    if opcao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        cal.divisao(n1,n2)

    if opcao == 5:
        print("\nSaindo do Sistema...")
