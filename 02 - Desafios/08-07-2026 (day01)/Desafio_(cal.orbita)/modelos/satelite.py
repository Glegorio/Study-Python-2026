class Satelite:
    """
    Representa um satélite artificial ou natural.
    """

    def __init__(self, nome: str, massa: float):
        self.nome = nome 
        self.massa = massa

    def __str__(self):
        return(
            f"Satélite: {self.nome}\n"
            f"Massa: {self.massa:.3e} kg"
        )