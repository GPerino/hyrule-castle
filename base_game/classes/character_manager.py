import json
import os

from .boss import Boss
from .enemy import Enemy
from .hero import Hero

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CharacterManager:
    """Manage character selection for hero, enemies, and bosses."""

    def __init__(self):
        self.rarity_weights = [0, 50, 30, 15, 4, 1]
        self.hero = Hero(0, "", 0, 0, 0, 0, 0)
        self.heroes_available = []
        self.enemy = Enemy("", 0, 0, 0, 0, 0)
        self.boss = Boss("", 0, 0, 0, 0, 0)

    def get_heroes(self):
        with open(BASE_DIR + "/data/heroes.json") as f:
            data = json.load(f)
        self.heroes_available = [
            Hero(**hero)
            for hero in data
        ]
        return self.heroes_available
