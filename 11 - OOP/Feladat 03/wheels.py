class Wheels:
    def __init__(self, brand: str, size: int, hardness: int):
        self.brand = brand
        self.size = size
        self.hardness = hardness

    def __str__(self)->str:
        return f"{self.brand}, {self.size} mm, {self.hardness}A"