#osztaly
class Motorcycle:
    #konstruktor
    def __init__(self):
        super().__init__()
        #adattagok
        self.manufacturer: str = None
        self.type: str = None
        self.model: str = None
        self.fuelConsumption: float = 0
        self.productionyear: int = 0
        self.horsePower: int = 0
        self.cylinders: int = 0
        self.torque: int = 0

    #magikus fuggveny / magic methods
    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model} ({self.productionyear})"
    