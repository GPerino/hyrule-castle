import json
import os

from .Boss import Boss
from .Enemy import Enemy
from .hero import Hero

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CharacterManager:
    """Manage character selection for hero, enemies, and bosses."""

    def __init__(self):
        self.rarity_weights = [0, 50, 30, 15, 4, 1]
        self.hero = Hero("", 0, 0, 0, 0, 0)
        self.heros_available = []
        self.enemy = Enemy("", 0, 0, 0, 0, 0)
        self.boss = Boss("", 0, 0, 0, 0, 0)

    def get_hero(self):
        with open(BASE_DIR + "/data/heros.json") as f:
            data = json.load(f)
            for hero in data:
                self.heros_available.append(hero)
        return self.heros_available
