class Calculadora:

    def soma(self, nmrUm, nmrDois):

        resultado = nmrUm + nmrDois
        print(f"A soma de {nmrUm} + {nmrDois} é = {resultado}") 

    def subtracao(self, nmrUm, nmrDois):
        
        resultado = nmrUm - nmrDois
        print(f"A subtração de {nmrUm} - {nmrDois} é = {resultado}") 

    def multiplicacao(self, nmrUm, nmrDois):
        
        resultado = nmrUm * nmrDois
        print(f"A multiplicação de {nmrUm} * {nmrDois} é = {resultado}") 

    def divisao(self, nmrUm, nmrDois):

        if nmrUm == 0:
            print("[ERRO] - Não é possível dividir por zero")

        elif nmrDois == 0:
            print("[ERRO] - Não é possível dividir por zero")

        else:
            resultado = nmrUm / nmrDois
            print(f"A divisão de {nmrUm} / {nmrDois} é = {resultado}") 

        