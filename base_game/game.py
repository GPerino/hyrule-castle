from collections import namedtuple

from base_game.classes.Character_manager import CharacterManager
from base_game.classes.Dungeon_manager import DungeonManager
from base_game.classes.Player import Player
from base_game.classes.Settings import GameSettings
from base_game.utils import clear_screen, show_intro, display_character_card


class Game:

    def __init__(self, audio):
        self.mode = "History"
        self.difficulty = "Normal"
        self.settings = GameSettings()
        self.manager = CharacterManager()
        self.dungeon_manager = DungeonManager()
        self.audio = audio
        self.is_running = False
        self.player = Player("", 0, 0, 0, 0, 0)

    def intro(self, stdscr):
        self.audio.play("menu")
        lines = [
            "Bienvenue au château d'Hyrule.",
            "",
            "Pour finir le jeu, tu dois reprendre le contrôle du Château d'Hyrule.",
            "",
            "Pour y arriver, des épreuves t'attendent à chaque salle…",
            "",
            "Ennemis, pièges, coffres, marchands : reste sur tes gardes.",
            "",
            "Mais vous avez votre épée, votre bouclier et quelques potions.",
            "",
            "Bonne chance, héros.",
        ]
        clear_screen(stdscr)
        show_intro(stdscr, lines, delay_ms=120)
        self.audio.stop()


    def start(self, stdscr):
        self.intro(stdscr)
        clear_screen(stdscr)
        stdscr.addstr(10, 65, f"Choisissez votre personnage")
        stdscr.refresh()
        PlayerTuple = namedtuple("Player", "id, name, hp, str_, def_, spd, luck")
        data = self.choose_character(stdscr)
        self.player = PlayerTuple(**data)
        stdscr.clear()
        stdscr.addstr(4, 65, f"Vous incarnez {self.player.name}")
        stdscr.addstr(6, 65, f"Appuyer pour continuer")
        stdscr.refresh()
        stdscr.getkey()
