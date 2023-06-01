from volleyballIO import *
from services import *
from volleyball import Volleyball
from os import *

filename: str = "data/adatok.txt"
players: List[Volleyball] = readPlayersFromFile(filename)

#- Írjuk ki a képernyőre az össz adatot
writeToConsole(players)

#- Keressük ki az ütő játékosokat az utok.txt állömányba
filteredPlayers: List[Volleyball] = getPlayersByPost("ütő", players)
writeToFile("utok.txt", filteredPlayers)

#- Rendezzük a játékosokat magasság szerint növekvő sorrendbe és a magaslatok.txt állományba mentsük el.

#- Mutassuk be a nemzetisegek.txt állományba, hogy mely nemzetiségek képviseltetik magukat a röplabdavilágban mint játékosok és milyen számban.

#- atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.

#- Állítsa növekvő sorrendbe a posztok szerint a játékosok ösz magasságát

#- Egy szöveges állományba, „alacsonyak.txt” keresse ki a játékosok átlagmagasságától alacsonyabb játékosokat. Az állomány tartalmazza a játékosok nevét,  magasságát és hogy mennyivel alacsonyabbak az átlagnál, 2 tizedes pontossággal.