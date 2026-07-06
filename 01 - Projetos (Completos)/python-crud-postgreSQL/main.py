from models.usuario import Usuario
from models.livros import Livros
from repository.livros_repository import LivrosRepository
from repository.usuario_repository import UsuarioRepository

opcao = 0

while opcao != 5:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Cadastrar Usuário")
    print("2 - Cadastrar Livro")
    print("3 - Listar Usuários Cadastrados")
    print("4 - Listar Livros Cadastrados")
    print("5 - Sair do Sistema")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        nome = str(input("\nDigite o nome do usuário: "))
        cpf = str(input("\nDigite o cpf do usuário: "))
        email = str(input("\nDigite o email do usuário: "))
        telefone = str(input("\nDigite o telefone do usuário: "))
        usuario = Usuario(nome, cpf, email, telefone)

        usuario = UsuarioRepository.cadastrar(usuario)

    elif opcao == 2:
        nome = str(input("\nDigite o nome do Livro: "))
        categoria = str(input("\nDigite a Categoria do Livro: "))
        autor = str(input("\nDigite o Autor do Livro: "))
        livro = Livros(nome, categoria, autor)

        livro = LivrosRepository.cadastrar(livro)

    elif opcao == 3:
        UsuarioRepository.listar()

    elif opcao == 4:
        LivrosRepository.listar()

    elif opcao == 5:
        print("\nEncerrando Sistema...")

    else:
        print("\nOpção inválida!")
    

    

