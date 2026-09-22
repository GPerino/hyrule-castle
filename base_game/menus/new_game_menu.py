from pick import pick

from base_game.classes import user_manager
from base_game.classes.Character_manager import CharacterManager
from base_game.classes.Player import Player
from base_game.game import Game
from base_game.utils import display_character_card


class NewGameMenu:
    def __init__(self):
        self.manager = CharacterManager()
        self.game = Game()
        self.player = Player()

    def choose_difficulty(self, stdscr):
        stdscr.clear()
        title = "Choisissez la difficulté"
        options = ["Facile", "Normal", "Hardcore"]
        level, _ = pick(options, title, screen=stdscr)
        self.game.difficulty = level

    def choose_game_mode(self, stdscr):
        stdscr.clear()
        title = "Choisissez le mode de jeu"
        options = ["Histoire", "Difficile", "Aléatoire"]
        # @TODO Afficher détails des options
        mode, _ = pick(options, title, screen=stdscr)
        self.game.mode = mode

    def choose_character(self, stdscr):
        characters = self.manager.get_characters()
        screen_h, screen_w = stdscr.getmaxyx()
        start_y = (screen_h // 2) - (10 // 2)
        start_x = (screen_w // 2) - (35 // 2)
        selected_index = 0
        while True:
            stdscr.clear()
            stdscr.addstr(start_y - 2, start_x + 4, f"Choisissez votre personnage")
            stdscr.refresh()
            display_character_card(stdscr, characters[selected_index], start_y, start_x)
            key = stdscr.getkey()
            if key == "KEY_UP":
                selected_index = (selected_index - 1) % len(characters)
            elif key == "KEY_DOWN":
                selected_index = (selected_index + 1) % len(characters)
            elif key == "\n":
                return characters[selected_index]

    def show_menu(self, stdscr):
        stdscr.clear()
        stdscr.addstr(1, 1, "Nouvelle Partie")
        stdscr.refresh()
        player_name = stdscr.getch()
        user_manager.new_user(player_name)
        stdscr.refresh()
        self.choose_game_mode(stdscr)
        self.choose_difficulty(stdscr)
        self.player.name = self.choose_character(stdscr)
