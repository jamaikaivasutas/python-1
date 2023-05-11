from board import Board
from trucks import Trucks
from wheels import Wheels
from bearings import Bearings
from griptape import Griptape

from skateboard import Skateboard

skateBoard: Board = Board("Toy Machine", "Bamboo", 7)
skateTrucks: Trucks = Trucks("Alien Workshop", "Complete (default ones)")
skateWheels: Wheels = Wheels("Mini Logo", 54, 102)
skateBearings: Bearings = Bearings("Bones", "Reds", "No ABEC rating")
skateGriptape: Griptape = Griptape("Jessup", "Medium")

skate: Skateboard = Skateboard(skateBoard, skateTrucks, skateWheels, skateBearings, skateGriptape)

print(skate)
