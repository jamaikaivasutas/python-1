class GPU:
    def __init__(self, manufacturer: str, model: str, vram: int, productionYear: int):
        self.manufacturer = manufacturer
        self.model = model
        self.vram = vram
        self.productionYear = productionYear

    def __str__(self) -> str:
        return f"{self.manufacturer}, {self.model}, {self.vram} GB, {self.productionYear}"