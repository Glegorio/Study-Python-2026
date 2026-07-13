class Planeta:
    """
    Representa um corpo celeste ESFÉRICO.
    """

    def __init__(self, nome: str, massa: float, raio: float):
        self.nome = nome 
        self.massa = massa 
        self.raio = raio

    def __str__(self):
        return(
            f"Planeta: {self.nome}\n"
            f"Massa: {self.massa:.3e} kg\n"
            f"Raio: {self.raio:,.0f} m"
        )