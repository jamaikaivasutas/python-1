class Music:
    def __init__(self, name: str, author: str, genre: str, length: float):
        self.name = name
        self.author = author
        self.genre = genre
        self.length = length

    def __str__(self)->str:
        return f"Name: {self.name}\nAuthor: {self.author}\nGenre: {self.genre}\nLenght: {self.length} Minutes"