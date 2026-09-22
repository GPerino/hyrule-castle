from pick import pick

from base_game.game import Game
from base_game.menus.new_game_menu import NewGameMenu
from base_game.menus.options_menu import OptionsMenu


class MainMenu:
    def __init__(self, audio):
        self.audio = audio
        self.game = Game(self.audio)

    def show(self, stdscr):
        options_menu = OptionsMenu()
        while True:
            title = "=== Menu Principal ==="
            options = ["Lancer une nouvelle partie", "Continuer une partie", "Gestions des joueurs" "Options",
                       "Quitter"]
            _, index = pick(options, title, screen=stdscr)
            if index == 0:
                NewGameMenu.show_menu(stdscr)
            elif index == 1:
                self.game.start(stdscr)
            elif index == 2:
                pass
            elif index == 3:
                pass
            elif index == 4:
                options_menu.show(stdscr)
            elif index == 5:
                return "Quit"
