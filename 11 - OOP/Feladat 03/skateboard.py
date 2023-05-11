from board import Board
from trucks import Trucks
from wheels import Wheels
from bearings import Bearings
from griptape import Griptape

class Skateboard:
    def __init__(self, board: Board, trucks: Trucks, wheels: Wheels, bearings: Bearings, griptape: Griptape):
        self.board = board
        self.trucks = trucks
        self.wheels = wheels
        self.bearings = bearings
        self.griptape = griptape

    def __str__(self)->str:
        return f"Board: {self.board}\nTrucks: {self.trucks}\nWheels: {self.wheels}\nBearings: {self.bearings}\nGriptape: {self.griptape}"
