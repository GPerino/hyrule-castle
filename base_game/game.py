from collections import namedtuple

from base_game.classes.Dungeon_manager import DungeonManager
from base_game.classes.Settings import GameSettings
from base_game.utils import clear_screen, show_intro, choose_character


class Game:

    def __init__(self, audio, mode, difficulty, hero):
        self.mode = mode
        self.difficulty = difficulty
        self.settings = GameSettings()
        self.hero = hero
        self.dungeon_manager = DungeonManager()
        self.audio = audio
        self.is_running = False

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
        HeroTuple = namedtuple("Hero", "id, name, hp, str_, def_, spd, luck")
        self.hero = HeroTuple(**self.hero)
        stdscr.addstr(4, 65, f"Vous incarnez {self.hero.name}")
        stdscr.addstr(6, 65, f"Appuyer pour continuer")
        stdscr.refresh()
        stdscr.getkey()
