from modelos.constantes import Constantes
from modelos.planeta import Planeta

from servicos.gravidade import GravidadeService
from servicos.velocidade import VelocidadeService


def mostrar_velocidade(planeta, altitude):

    velocidade = (
        VelocidadeService
        .calcular_velocidade_orbital(
            planeta,
            altitude
        )
    )

    velocidade_kmh = (
        VelocidadeService
        .converter_para_kmh(
            velocidade
        )
    )

    print("-" * 60)
    print(f"Planeta: {planeta.nome}")
    print(f"Altitude: {altitude:,.0f} m")
    print(f"Velocidade: {velocidade:.2f} m/s")
    print(f"Velocidade: {velocidade_kmh:,.2f} km/h")


def main():

    terra = Planeta(
        "Terra",
        Constantes.MASSA_TERRA,
        Constantes.RAIO_TERRA
    )

    lua = Planeta(
        "Lua",
        Constantes.MASSA_LUA,
        Constantes.RAIO_LUA
    )

    mostrar_velocidade(
        terra,
        408_000
    )

    mostrar_velocidade(
        lua,
        100_000
    )


if __name__ == "__main__":
    main()