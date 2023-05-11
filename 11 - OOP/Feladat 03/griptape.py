class Griptape:
    def __init__(self, brand: str, grip: str):
        self.brand = brand
        self.grip = grip

    def __str__(self)->str:
        return f"{self.brand}, {self.grip}"