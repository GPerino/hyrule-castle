import time

from base_game.classes.dungeon_manager import DungeonManager
from base_game.classes.hero import Hero
from base_game.classes.save_manager import SaveManager
from base_game.classes.settings import GameSettings
from base_game.utils import clear_screen, show_intro


class Game:
    def __init__(self, audio, mode: str, difficulty: str, hero: Hero):
        self.mode = mode
        self.difficulty = difficulty
        self.last_save = time.time()
        self.settings = GameSettings()
        self.hero = hero
        self.dungeon_manager = DungeonManager()
        self.audio = audio
        self.is_running = False

    def to_dict(self):
        return {
            "metadata": {
                "last_save": self.last_save
            },
            "game": {
                "mode": self.mode,
                "difficulty": self.difficulty,
                "progression": self.dungeon_manager.get_progression()
            },
            "character": self.hero.to_dict()
        }

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
        stdscr.addstr(4, 65, f"Vous incarnez {self.hero.name}")
        stdscr.addstr(6, 65, f"Appuyer pour continuer")
        stdscr.refresh()
        stdscr.getkey()

    def handle_exit(self, stdscr):
        save_manager = SaveManager()
        stdscr.addstr("\nSaving your progress...")
        save_manager.save_game(self, "save_exit")
        # @TODO: Ajouter une logique de sauvegarde
        stdscr.addstr("Progress saved.")
        stdscr.addstr("Goodbye, adventurer!")
