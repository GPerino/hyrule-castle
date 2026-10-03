from enum import Enum


class Room(Enum):
    START = "start"
    ENEMY = "enemy"
    ELITE = "elite"
    BOSS = "boss"
    PUZZLE = "puzzle"
    CHEST = "chest"
    TRAP = "trap"
    MERCHANT = "merchant"