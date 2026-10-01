import json
import os
import random

from base_game.classes.Room import Room
from base_game.classes.character_manager import CharacterManager
from base_game.classes.enemy import Enemy

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
            # pass
            stdscr.addstr(1, 60, room)
            stdscr.refresh()
            stdscr.getkey()
        elif room is Room.ENEMY:
            stdscr.addstr(1, 60, room)
            enemy = self.choose_enemy(dungeon)
            stdscr.addstr(3, 60, enemy.name)
            stdscr.refresh()
            stdscr.getkey()
        elif room is Room.CHEST:
            stdscr.addstr(1, 60, room)
            stdscr.refresh()
            stdscr.getkey()
        elif room is Room.PUZZLE:
            stdscr.addstr(1, 60, room)
            stdscr.refresh()
            stdscr.getkey()
        elif room is Room.MERCHANT:
            stdscr.addstr(2, 60, room)
            stdscr.refresh()
            stdscr.getkey()
        elif room is Room.ELITE:
            elite = self.choose_elite(dungeon)
            stdscr.addstr(4, 60, elite.name)
            stdscr.refresh()
            stdscr.getkey()
        elif room is Room.BOSS:
            boss = self.get_dungeon_boss(dungeon)
            stdscr.addstr(5, 60, boss.name)
            stdscr.refresh()
            stdscr.getkey()

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

    def choose_enemy(self, dungeon) -> Enemy:
        enemies = self.get_list_enemies(dungeon)
        enemy = random.choice(enemies)
        return enemy

    def choose_elite(self, dungeon) -> Enemy:
        elites = self.get_list_elites(dungeon)
        elite = random.choice(elites)
        return elite

    def get_list_elites(self, dungeon):
        elites = dungeon.get("elites")
        dungeon_elites = []
        manager = CharacterManager()
        all_enemies = manager.load_enemies()
        for enemy in all_enemies:
            if enemy.id in elites:
                dungeon_elites.append(enemy)
        return dungeon_elites

    def get_dungeon_boss(self, dungeon):
        boss = dungeon.get("boss")
        manager = CharacterManager()
        all_bosses = manager.load_bosses()
        for load_boss in all_bosses:
            if load_boss.id == boss:
                dungeon_boss = load_boss
        return dungeon_boss