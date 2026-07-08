from database.inicializar_banco import InicializarBanco
from services.cadastro_service import CadastroService


def main():

    InicializarBanco().criar_tabelas()

    cadastro = CadastroService()

    participante = cadastro.cadastrar(

        nome="Maria Oliveira",

        cpf="98765432100",

        email="maria@email.com",

        telefone="16999999999",

        empresa="Empresa X",

        cargo="Gerente"

    )

    print()

    print("Cadastro realizado!")

    print()

    print(participante)

    print()

    print("QR Code:", participante.qr_code)


if __name__ == "__main__":
    main()