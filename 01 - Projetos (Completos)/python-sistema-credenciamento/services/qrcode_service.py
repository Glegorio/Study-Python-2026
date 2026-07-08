import os
import qrcode
from repositories.participante_repository import ParticipanteRepository 

class QRCodeService:

    def __init__(self):
        self.repository = ParticipanteRepository()

    def gerar_qrcode(self, participante):

        os.makedirs("qrcodes", exist_ok=True)

        imagem = qrcode.make(participante.uuid)

        nome_arquivo = f"{participante.uuid}.png"

        caminho = os.path.join(
            "qrcodes",
            nome_arquivo 
        )

        imagem.save(caminho)

        participante.qr_code = nome_arquivo

        self.repository.atualizar(participante)

        return caminho