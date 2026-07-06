from database.connection import Connection

class LivrosRepository:

    @staticmethod
    def cadastrar(livros):

        conexao = Connection.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO livros
            (nome, categoria, autor)
            VALUES (%s, %s, %s)
        """

        valores = (
            livros.nome,
            livros.categoria,
            livros.autor
        )

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()

        conexao.close()

        print("Livro Cadastrado com Sucesso")

    @staticmethod
    def listar():

        conexao = Connection.conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT * FROM livros
            ORDER BY id;
        """

        cursor.execute(sql)

        livros = cursor.fetchall()

        cursor.close()
        conexao.close()

        print("-" * 100)

        print(
            f"| {'ID':<5}"
            f"| {'NOME':<25}"
            f"| {'CATEGORIA':<35}"
            f"| {'AUTOR':<35}"
        )

        print("-" * 100)

        for livros in livros:

            print(
                f"| {livros[0]:<5}"
                f"| {livros[1]:<25}"
                f"| {livros[2]:<35}"
                f"| {livros[3]:<35}"
            )
        
        print("-" * 100)


