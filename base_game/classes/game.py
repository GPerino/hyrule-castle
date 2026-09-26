from datetime import datetime

from base_game.classes.dungeon_manager import DungeonManager
from base_game.classes.hero import Hero
from base_game.classes.settings import GameSettings
from base_game.utils import clear_screen, show_intro


class Game:
    def __init__(self, audio, mode: str, difficulty: str, hero: Hero, progression=None):
        if progression is None:
            progression = {
                "dungeon": 1,
                "room": 1
            }
        self.mode = mode
        self.difficulty = difficulty
        self.last_save = datetime.now()
        self.hero = hero
        self.progression = progression
        self.settings = GameSettings()
        self.dungeon_manager = DungeonManager()
        self.audio = audio
        self.is_running = False

    @classmethod
    def from_dict(cls, data, hero, audio):
        game = cls(
            audio=audio,
            mode=data["mode"],
            difficulty=data["difficulty"],
            hero=hero,
            progression=data["progression"]
        )
        return game

    def to_dict(self):
        return {
            "metadata": {
                "last_save": self.last_save.strftime("%m/%d/%Y, %H:%M:%S")
            },
            "game": {
                "mode": self.mode,
                "difficulty": self.difficulty,
                "progression": self.progression
            },
            "hero": self.hero.to_dict()
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
        clear_screen(stdscr)
        self.browse_dungeons(stdscr)
        # stdscr.addstr(2, 65, f"Détails de la partie")
        # stdscr.addstr(4, 65, f"Vous incarnez {self.hero.name}")
        # stdscr.addstr(5, 65, f"Mode {self.mode}")
        # stdscr.addstr(6, 65, f"Difficulté {self.difficulty}")
        # stdscr.addstr(7, 65, f"Donjon {self.progression['dungeon']}")
        # stdscr.addstr(8, 65, f"Salle {self.progression['room']}")
        # stdscr.addstr(12, 65, f"Appuyer pour continuer")
        stdscr.refresh()
        stdscr.getkey()

    def browse_dungeons(self, stdscr):
        dungeons = self.dungeon_manager.dungeons
        for dungeon in dungeons:
            self.browse_rooms(stdscr, dungeon)
            stdscr.refresh()
            stdscr.getkey()

    def browse_rooms(self, stdscr, dungeon):
        rooms = dungeon.get("rooms")
        for room in rooms:
            self.dungeon_manager.launch_room(stdscr, dungeon, room)
            stdscr.refresh()
            stdscr.getkey()
            clear_screen(stdscr)