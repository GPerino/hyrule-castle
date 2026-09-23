import curses

from base_game.classes.character_manager import CharacterManager
from base_game.classes.hero import Hero
from base_game.classes.save_manager import SaveManager
from base_game.classes.user_manager import new_user
from base_game.game import Game
from base_game.utils import choose_game_mode, choose_difficulty, choose_character, draw_box


class NewGameMenu():
    def __init__(self, audio):
        self.manager = CharacterManager()
        self.audio = audio
        self.hero = Hero("", 0, 0, 0, 0, 0)

    def show_menu(self, stdscr):
        stdscr.clear()
        user_name = ""
        user = True
        while user_name == "" or user is None:
            stdscr.clear()
            stdscr.refresh()
            draw_box(stdscr, 4, 10, 3, 30, "Tapez le nom du joueur")
            stdscr.addstr(5, 12, "> ")
            curses.echo()
            user_name = stdscr.getstr(5, 15).decode("utf-8")
            user = new_user(user_name, stdscr)
            curses.noecho()
        mode = choose_game_mode(stdscr)
        difficulty = choose_difficulty(stdscr)
        self.hero = choose_character(stdscr)
        game = Game(self.audio, mode, difficulty, self.hero)
        save_manager = SaveManager()
        save_manager.save_game(user, game)
        game.start(stdscr)
