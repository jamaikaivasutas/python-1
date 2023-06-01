from volleyball import Volleyball
import os
from typing import *
from io import open

def readPlayersFromFile(fileName: str) -> List[Volleyball]:
    players: List[Volleyball] = []
    player: Volleyball = None

    basepath: str = os.path.dirname(os.path.abspath(__file__))
    fileFullPath: str = os.path.join(basepath, fileName)

    try:
        with open(fileFullPath,encoding="utf-8", mode="r") as file:
            for line in file:
                oneLine = line.strip() 
                data = oneLine.split('\t')
        
                player = Volleyball()
                player.name: str = data[0]
                player.height: int = data[1]
                player.post: str = data[2]
                player.nationality: str = data[3]
                player.team: str = data[4]
                player.country: str = data[5]
                
                players.append(player)

        return players
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []

def writeToFile(filename: str, players: List[Volleyball])->None:
    basepath: str = os.path.dirname(os.path.abspath(__file__))
    basepath += "/output"
    fileFullPath: str = os.path.join(basepath, filename)

    try:
        with open(fileFullPath,encoding="utf-8", mode="w") as file:
            for player in players:
                file.write(f"{player.name}\t{player.height}\t{player.post}\t{player.nationality}\t{player.team}\t{player.country}\n")

    except FileNotFoundError as ex:
        print(f"{ex.filename} iraskor hiba lepett fel")
