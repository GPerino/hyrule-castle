import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DungeonManager:
    dungeons = []

    def __init__(self):
        with open(BASE_DIR + '/data/dungeons.json', 'r') as file:
            self.dungeons = json.load(file).get('dungeons')
        self.current_dungeon = None
