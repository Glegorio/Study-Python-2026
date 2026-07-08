from database.conexao import Conexao
from models.participante import Participante

class ParticipanteRepository:

    def __init__(self):
        self.conexao = Conexao()

    def salvar(self, participante: Participante):

        banco = self.conexao.conectar()

        cursor = banco.cursor()

        cursor.execute("""
            INSERT INTO participantes
            (
                uuid,
                nome,
                cpf,
                email,
                telefone,
                empresa,
                cargo,
                qr_code,
                entrada_realizada,
                data_entrada,
                hora_entrada,
                criado_em,
                cracha
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            
            participante.uuid,
            participante.nome,
            participante.cpf,
            participante.email,
            participante.telefone,
            participante.empresa,
            participante.cargo,
            participante.qr_code,
            int(participante.entrada_realizada),
            participante.data_entrada,
            participante.hora_entrada,
            participante.criado_em,
            participante.cracha
        ))

        banco.commit()

        participante.id = cursor.lastrowid

        banco.close()

        return participante
    
    def buscar_por_id(self, id):

        banco = self.conexao.conectar()

        cursor = banco.cursor()

        cursor.execute(
            "SELECT * FROM participantes WHERE id = ?",
            (id,)
        )

        resultado = cursor.fetchone()

        banco.close()

        if resultado:
            return Participante.from_dict(dict(resultado))
        
        return None
    
    def buscar_por_cpf(self, cpf):

        banco = self.conexao.conectar()

        cursor = banco.cursor()

        cursor.execute(
            "SELECT * FROM participantes WHERE cpf =?",
            (cpf,)
        )

        resultado = cursor.fetchone()

        banco.close()

        if resultado:
            return Participante.from_dict(dict(resultado))
        
        return None

    def buscar_por_uuid(self, uuid):

        banco = self.conexao.conectar()

        cursor = banco.cursor()

        cursor.execute(
            "SELECT * FROM participantes WHERE uuid = ?",
            (uuid,)
        )

        resultado = cursor.fetchone()

        banco.close()

        if resultado:
            return Participante.from_dict(dict(resultado))

        return None

    def listar_todos(self):

        banco = self.conexao.conectar()

        cursor = banco.cursor()

        cursor.execute("""
            SELECT *
            FROM participantes
            ORDER BY nome
        """)

        resultados = cursor.fetchall()

        banco.close()

        participantes = []

        for registro in resultados:

            participantes.append(
                Participante.from_dict(dict(registro))
            )
        
        return participantes

    def atualizar(self, participante: Participante):

        banco = self.conexao.conectar()

        cursor = banco.cursor()

        cursor.execute("""
            UPDATE participantes
            SET
                nome=?,
                cpf=?,
                email=?,
                telefone=?,
                empresa=?,
                cargo=?,
                qr_code=?,
                entrada_realizada=?,
                data_entrada=?,
                hora_entrada=?,
                cracha=?
            
            WHERE id=?
        """, (
            participante.nome,
            participante.cpf,
            participante.email,
            participante.telefone,
            participante.empresa,
            participante.cargo,
            participante.qr_code,
            int(participante.entrada_realizada),
            participante.data_entrada,
            participante.hora_entrada,
            participante.id,
            participante.cracha
        ))

        banco.commit()

        banco.close()

    def excluir(self, id):

        banco = self.conexao.conectar()

        cursor = banco.cursor()

        cursor.execute(
            "DELETE FROM participantes WHERE id = ?",
            (id,)
        )

        banco.commit()

        banco.close()