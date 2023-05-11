class Speaker:
    def __init__(self, brand: str, model: str, type: str, output: int):
        self.brand = brand
        self.model = model
        self.type = type
        self.output = output

    def __str__(self)->str:
        return f"Brand: {self.brand}\nModel: {self.model}\nType: {self.type}\nOutput: {self.output} W"