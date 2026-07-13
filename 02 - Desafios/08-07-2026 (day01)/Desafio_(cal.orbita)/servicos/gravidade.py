from modelos.constantes import Constantes 
from modelos.planeta import Planeta 

class GravidadeService:
    """
    Classe responsável pelos cálculos 
    relacionados à gravidade.
    """

    @staticmethod
    def calcular_forca(planeta: Planeta, massa_objeto: float, distancia: float) -> float:
        """
        Calcula a força gravitacional.

        Fórmula: F = G * M * m / r²
        """

        if distancia <= 0:
            raise ValueError("A distância deve ser maior que zero.")

        if massa_objeto <= 0:
            raise ValueError("A massa do objeto deve ser maior que zero.")

        return(
            Constantes.G 
            * planeta.massa 
            * massa_objeto
        ) / (distancia ** 2)
    
    @staticmethod
    def calcular_gravidade_superficie(planeta: Planeta) -> float:
        """
        Calcula a aceleração da gravidade
        na superfície.

        Fórmula: g = GM / r²
        """

        return(
            Constantes.G 
            * planeta.massa
        ) / (planeta.raio ** 2)

    @staticmethod
    def calcular_peso(planeta: Planeta, massa_objeto: float) -> float:
        """
        Peso = massa x gravidade
        """

        g = GravidadeService.calcular_gravidade_superficie(planeta)

        return massa_objeto * g 