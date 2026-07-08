import sqlite3

class Conexao:

    def __init__(self):
        self.caminho_banco = "database/banco.db"

    def conectar(self):
        conexao = sqlite3.connect(self.caminho_banco)

        conexao.row_factory = sqlite3.Row 

        return conexao
    
