from database.conexao import Conexao

class InicializarBanco:

    def __init__(self):
        self.conexao = Conexao()

    def criar_tabelas(self):

        banco = self.conexao.conectar()

        cursor = banco.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS participantes(

                id                  INTEGER     PRIMARY KEY AUTOINCREMENT,
                uuid                TEXT        NOT NULL UNIQUE,
                nome                TEXT        NOT NULL,
                cpf                 TEXT        NOT NULL UNIQUE,         
                email               TEXT        NOT NULL,
                telefone            TEXT,   
                empresa             TEXT, 
                cargo               TEXT,
                qr_code             TEXT,
                entrada_realizada   INTEGER     DEFAULT 0,
                data_entrada        TEXT,
                hora_entrada        TEXT,
                criado_em           TEXT        NOT NULL
            );
        """)

        banco.commit()

        banco.close()