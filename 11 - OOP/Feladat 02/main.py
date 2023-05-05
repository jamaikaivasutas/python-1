from cpu import CPU
from gpu import GPU
from motherboard import Motherboard
from ram import Ram
from computer import Computer

computerProcessor: CPU = CPU("Intel", "i7-7700HQ", 3.8, 2017)
computerGraphicsCard: GPU = GPU("GeForce", "GTX-1060", 2, 2015)
computerRam: Ram = Ram("MSI", 16)
computerMotherboard: Motherboard = Motherboard("MSI", "G4P-MRV")

computer: Computer = Computer(computerRam, computerProcessor, computerGraphicsCard, computerMotherboard)

print(computer)