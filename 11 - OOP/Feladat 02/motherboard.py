class Motherboard:
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model

    def __str__(self) -> str:
        return f"{self.manufacturer}, {self.model}"