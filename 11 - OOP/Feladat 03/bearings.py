class Bearings:
    def __init__(self, brand: str, model: str, type: str):
        self.brand = brand
        self.model = model
        self.type = type

    def __str__(self)->str:
        return f"{self.brand}, {self.model}, {self.type}"