import math 

from modelos.constantes import Constantes 
from modelos.planeta import Planeta 

class VelocidadeService:
    """
    Serviço responsável pelos cálculos de velocidade.
    """

    @staticmethod
    def calcular_velocidade_orbital(planeta: Planeta, altitude: float = 0) -> float:
        """
        Calcula a velocidade orbital circular.

        Fórmula: v = sqrt(GM/r)

        altitude em metros.
        """

        if altitude < 0:
            raise ValueError("A altitude não pode ser negativa")

        distancia = planeta.raio + altitude

        velocidade = math.sqrt(
            (
                Constantes.G 
                * planeta.massa
            ) / distancia
        )

        return velocidade

    @staticmethod
    def converter_para_kmh(velocidade_ms: float) -> float:
        """
        Converte m/s para km/h.
        """

        return velocidade_ms * 3.6