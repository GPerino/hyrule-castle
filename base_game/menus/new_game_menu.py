import curses

from base_game.classes.Character_manager import CharacterManager
from base_game.classes.Player import Player
from base_game.classes.Save_manager import SaveManager
from base_game.classes.user_manager import new_user
from base_game.game import Game
from base_game.utils import display_character_card, choose_game_mode, choose_difficulty, choose_character


class NewGameMenu():
    def __init__(self, audio):
        self.manager = CharacterManager()
        self.audio = audio
        self.player = Player("", 0, 0, 0, 0, 0)

    def show_menu(self, stdscr):
        stdscr.clear()
        player_name = ""
        new_user_name = True
        while player_name == "" or new_user_name is None:
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(1, 10, "Tapez le nom du joueur")
            stdscr.addstr(3, 13, "> ")
            curses.echo()
            player_name = stdscr.getstr(3, 15).decode("utf-8")
            new_user_name = new_user(player_name, stdscr)
            curses.noecho()
        mode = choose_game_mode(stdscr)
        difficulty = choose_difficulty(stdscr)
        self.player = choose_character(stdscr)
        game = Game(self.audio, mode, difficulty, self.player)
        save_manager = SaveManager()
        save_manager.save_game(game)
        game.start(stdscr)
