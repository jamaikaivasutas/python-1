class Board:
    def __init__(self, brand: str, material: str, layers: int):
        self.brand = brand
        self.material = material
        self.layers = layers

    def __str__(self)->str:
        return f"{self.brand}, {self.material}, {self.layers}"