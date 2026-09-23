from pick import pick

from base_game.menus.load_game_menu import LoadGameMenu
from base_game.menus.new_game_menu import NewGameMenu
from base_game.menus.options_menu import OptionsMenu


class MainMenu:
    def __init__(self, audio):
        self.audio = audio
    def show(self, stdscr):
        options_menu = OptionsMenu()
        while True:
            title = "=== Menu Principal ==="
            options = ["Lancer une nouvelle partie", "Continuer une partie", "Gestions des sauvegardes", "Options",
                       "Quitter"]
            _, index = pick(options, title, screen=stdscr)
            if index == 0:
                new_game = NewGameMenu(self.audio)
                new_game.show_menu(stdscr)
            elif index == 1:
                load_game = LoadGameMenu(self.audio)
                load_game.show_menu(stdscr)
            elif index == 2:
                pass
            elif index == 3:
                options_menu.show(stdscr)
            elif index == 4:
                return "Quit"
