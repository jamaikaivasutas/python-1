from volleyball import Volleyball
from typing import *

def writeToConsole(players: List[Volleyball]) -> None:
    for player in players:
        print(player)

def getPlayersByPost(post: str ,players: List[Volleyball]) -> List[Volleyball]:
    filteredPlayers: List[Volleyball] = []
    
    for player in players:
        if(player.post == post):
            filteredPlayers.append(player)

    return filteredPlayers

