class Trucks:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def __str__(self)->str:
        return f"{self.brand}, {self.model}"