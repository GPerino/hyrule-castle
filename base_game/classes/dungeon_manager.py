import json
import os

from base_game.classes.Room import Room
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
        if room is Room.START:
            stdscr.addstr(1, 60, room)
        elif room is Room.ENEMY:
            stdscr.addstr(1, 60, room)
            self.get_list_enemies(dungeon)
        elif room is Room.ELITE:
            self.get_list_elites(dungeon)

    def get_list_enemies(self, dungeon):
        enemies = dungeon.get("enemies")
        elites = dungeon.get("elites")
        dungeon_elites = []
        dungeon_enemies = []
        manager = CharacterManager()
        all_enemies = manager.load_enemies()
        for enemy in all_enemies:
            if enemy.id in enemies:
                dungeon_enemies.append(enemy)
            if enemy.id in elites:
                dungeon_elites.append(enemy)
        return dungeon_enemies, dungeon_elites

    def get_list_elites(self, dungeon):
        elites = dungeon.get("elites")
        dungeon_elites = []
        manager = CharacterManager()
        all_enemies = manager.load_enemies()
        for enemy in all_enemies:
            if enemy.id in elites:
                dungeon_elites.append(enemy)
        return dungeon_elites
