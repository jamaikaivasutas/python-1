class CPU:
    def __init__(self, manufacturer: str, model: str, clockSpeed: float, productionYear: int):
        self.manufacturer = manufacturer
        self.model = model
        self.clockSpeed = clockSpeed
        self.productionYear = productionYear

    def __str__(self) -> str:
        return f"{self.manufacturer}, {self.model}, {self.clockSpeed} GHz, {self.productionYear}"