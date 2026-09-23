import glob
import json
import os

from pick import pick

from base_game.classes.game import Game
from base_game.classes.save import Save

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LoadGameMenu:
    def __init__(self, audio):
        self.audio = audio

    def choose_save_to_load(self, stdscr):
        saves = []

        for file in glob.glob(BASE_DIR + "/saves/*.json"):
            with open(file, "r") as f:
                data = json.load(f)

            save = Save.from_dict(data, self.audio)
            saves.append((save, file))

        options = [
            (
                f"{save.game.hero.name} | "
                f"{save.game.mode} | "
                f"{save.game.difficulty} | "
                f"Donjon {save.game.progression['dungeon']} - "
                f"Salle {save.game.progression['room']} | "
                f"{save.metadata['last_save']}"
            )
            for save, _ in saves
        ]

        selected, index = pick(
            options,
            "Choisissez une sauvegarde :",
            indicator="➜ ",
            screen=stdscr
        )

        save, file = saves[index]

        return save

    def show_menu(self, stdscr):
        stdscr.clear()
        save = self.choose_save_to_load(stdscr)
        game = self.load_game(save, stdscr)
        game.start(stdscr)
    def load_game(self, save, stdscr):
        game = Game(self.audio, save.game.mode, save.game.difficulty, save.game.hero, save.game.progression)
        return game
