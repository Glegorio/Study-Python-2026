import psycopg2

class Connection:

    @staticmethod
    def conectar():

        try:
            conexao = psycopg2.connect(
                host="localhost",
                database="python-crud",
                user="postgres",
                password="minhasenha123",
                port="5432"
            )
            
            print("Conexão realizado com sucesso!")

            return conexao
        
        except psycopg2.Error as erro:
            print("Erro ao conectar ao banco!")
            
            print(erro)
            
            return None