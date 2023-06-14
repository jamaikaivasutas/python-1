class Grade:
    def __init__(self):
        super().__init__()

        self.firstName: str = None
        self.lastName: str = None
        self.year: str = None
        self.grade: int = None

    def __str__(self)->str:
        return f"Neve: {self.firstName} {self.lastName}, osztálya: {self.year}, jegy: {self.grade}"

