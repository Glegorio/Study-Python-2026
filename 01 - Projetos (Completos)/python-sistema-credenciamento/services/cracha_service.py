import os 
from PIL import Image, ImageDraw, ImageFont 
from repositories.participante_repository import ParticipanteRepository

class CrachaService:

    def __init__(self):
        self.repository = ParticipanteRepository()

    def gerar_cracha(self, participante):

        os.makedirs("crachas", exist_ok=True)

        imagem = Image.new("RGB", (500,700), "white")

        desenho = ImageDraw.Draw(imagem)

        fonte = ImageFont.load_default()

        desenho.text((140,30), "EVENTO PYTHON", fill="black", font=fonte)
        desenho.text((30,100), f"Nome: {participante.nome}", fill="black", font=fonte)
        desenho.text((30,140), f"Empresa: {participante.empresa}", fill="black", font=fonte)
        desenho.text((30,180), f"Cargo: {participante.cargo}", fill="black", font=fonte)
        desenho.text((30,220), f"ID: {participante.id}", fill="black", font=fonte)

        qr = Image.open(
            os.path.join(
                "qrcodes",
                participante.qr_code
            )
        )

        qr = qr.resize((220,220))
        imagem.paste(qr,(140,320))
        nome_arquivo = f"crache_{participante.uuid}.png"

        caminho = os.path.join(
            "crachas",
            nome_arquivo
        )

        imagem.save(caminho)
        participante.cracha = nome_arquivo
        self.repository.atualizar(participante)

        return caminho
