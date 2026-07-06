from database.connection import Connection 

class UsuarioRepository:

    @staticmethod
    def cadastrar(usuario):

        conexao = Connection.conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO usuarios
            (nome, cpf, email, telefone)
            VALUES (%s, %s, %s, %s)
        """

        valores = (
            usuario.nome,
            usuario.cpf,
            usuario.email,
            usuario.telefone
        )
        
        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()

        conexao.close()

        print("Usuário Cadastrado com Sucesso!")
    
    @staticmethod
    def listar():

        conexao = Connection.conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT * FROM usuarios
            ORDER BY id;
        """

        cursor.execute(sql)

        usuarios = cursor.fetchall()

        cursor.close()
        conexao.close()

        print("-" * 110)

        print(
            f"| {'ID':<5}"
            f"| {'NOME':<25}"
            f"| {'CPF':18}"
            f"| {'EMAIL':<35}"
            f"| {'TELEFONE':<20}"
        )

        print("-" * 110)

        for usuario in usuarios:

            print(
                f"| {usuario[0]:<5}"
                f"| {usuario[1]:<25}"
                f"| {usuario[2]:<18}"
                f"| {usuario[3]:<35}"
                f"| {usuario[4]:<20}"
            )

        print("-" * 110)