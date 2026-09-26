import json
import os

from base_game.classes.character_manager import CharacterManager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DungeonManager:
    dungeons = []

    def __init__(self):
        with open(BASE_DIR + '/data/dungeons.json', 'r') as file:
            self.dungeons = json.load(file).get('dungeons')
            self.rooms = []
        self.current_dungeon = None

    def launch_room(self, stdscr, dungeon, room):
        if room.get("type") == "start":
            stdscr.addstr(1, 60, "start")
        elif room.get("type") == "enemy":
            stdscr.addstr(1, 60, "enemy")
            self.get_list_enemies(dungeon)
        elif room.get("type") == "elite":
            stdscr.addstr(1, 60, "elite")
            # self.get_list_enemies(dungeon)
        elif room.get("type") == "boss":
            stdscr.addstr(1, 60, "boss")
        #             self.get_list_enemies(dungeon)
        elif room.get("type") == "chest":
            stdscr.addstr(1, 60, "chest")
        elif room.get("type") == "merchant":
            stdscr.addstr(1, 60, "merchant")

    def get_list_enemies(self, dungeon):
        enemies = dungeon.get("enemies")
        manager = CharacterManager()
        manager.load_enemies()