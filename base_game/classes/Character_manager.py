import json
import os

from .Boss import Boss
from .Enemy import Enemy
from .Player import Player

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CharacterManager:
    """Manage character selection for player, enemies, and bosses."""

    def __init__(self):
        self.rarity_weights = [0, 50, 30, 15, 4, 1]
        self.player = Player("", 0, 0, 0, 0, 0)
        self.characters_available = []
        self.enemy = Enemy("", 0, 0, 0, 0, 0)
        self.boss = Boss("", 0, 0, 0, 0, 0)

    def get_characters(self):
        with open("/base_game/data/characters.json") as f:
            data = json.load(f)
            for player in data:
                self.characters_available.append(player)
        return self.characters_available
