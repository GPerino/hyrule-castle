from base_game.classes.hero import Hero
from base_game.classes.save_manager import SaveManager
from base_game.game import Game
from base_game.utils import choose_game_mode, choose_difficulty, choose_character


class NewGameMenu():
    def __init__(self, audio):
        self.audio = audio
        self.hero = Hero(0, "", 0, 0, 0, 0, 0)

    def show_menu(self, stdscr):
        stdscr.clear()
        mode = choose_game_mode(stdscr)
        difficulty = choose_difficulty(stdscr)
        self.hero = choose_character(stdscr)
        game = Game(self.audio, mode, difficulty, self.hero)
        try:
            game.start(stdscr)
        except KeyboardInterrupt:
            game.handle_exit(stdscr)