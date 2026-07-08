from models.participante import Participante
from repositories.participante_repository import ParticipanteRepository

from utils.uuid_generator import gerar_uuid
from utils.datas import data_hora_atual
from utils.validadores import email_valido
from services.qrcode_service import QRCodeService
from services.cracha_service import CrachaService

class CadastroService:

    def __init__(self):
        self.repository = ParticipanteRepository()
        self.qrcode_service = QRCodeService()
        self.cracha_service = CrachaService()

    def cadastrar(self, nome, cpf, email, telefone, empresa, cargo):
        
        if self.repository.buscar_por_cpf(cpf):
            raise ValueError(
                "[ERRO] - Já existe um participante com este CPF"
            )
        
        if not email_valido(email):
            raise ValueError(
                "[ERRO] - E-mail inválido"
            )

        participante = Participante(
            nome = nome,
            cpf = cpf,
            email = email,
            telefone = telefone,
            empresa = empresa,
            cargo = cargo,
            uuid = gerar_uuid(),
            criado_em = data_hora_atual()
        )

        participante = self.repository.salvar(participante)

        self.qrcode_service.gerar_qrcode(participante)

        self.cracha_service.gerar_cracha(participante)

        return participante