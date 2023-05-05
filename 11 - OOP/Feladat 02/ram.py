class Ram:
    def __init__(self, manufacturer: str, capacity: int):
        self.manufacturer = manufacturer
        self.capacity = capacity

    def __str__(self) -> str:
        return f"{self.manufacturer}, {self.capacity} GB"