import glob
import json
import os

from base_game.classes.User import User
from base_game.utils import check_special_characters

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def print_all_users():
    """
    return all user in users.json
    :return:
    """
    users = get_user_files()
    for user in users:
        print(user["username"])
    return users


def get_user_files():
    """
    create a string array with all json file name corresponding to all usernames
    :return:array
    """
    users = []
    for file in glob.glob(BASE_DIR + "/users/*.json"):
        users.append(file)
    return users


def new_user(username, stdscr):
    """
    Create a new user with class User
    :param username:
    :return: user:User
    """
    users = get_user_files()  # Get all username
    if not users.__contains__(BASE_DIR + "/users/" + username +".json"):  # Check if username is free
        user = User(username)  # Create user
        user.username = username
        save_user(user)  # Save user json file wit info
        return user
    else:
        stdscr.addstr(4, 4, f"User {username} already exists. ")
        stdscr.refresh()
        stdscr.getkey()
        return None

def save_user(user: User):
    """
    Create a json file with user's information
    :param user:
    :return:
    """
    users = get_user_files()
    username = user.username
    file_name = user.username + ".json"
    users.append(file_name)
    json_string = {
        "username": username,
    }
    file = open( BASE_DIR + "/users/" + file_name, "w")
    json.dump(json_string, file, indent=2)
    file.close()

def delete_user(username: str):
    users = get_user_files()
    filename = username + ".json"
    if users.__contains__(filename):
        os.remove(filename)  # Remove the user's json file
        print(f"User {username} has been successfully deleted")
    else:
        print("This user doesn't exist")




def users_menu():
    """
    Display users' manager menu and execute function with user's choice  or return to main menu
    :return: int
    """
    manage_choice = 0
    while (
            manage_choice != 1
            and manage_choice != 2
            and manage_choice != 3
            and manage_choice != 4
    ):
        manage_choice = input("""
        [1] - Display users list      
        [2] - Create a new user
        [3] - Delete a user
        [4] - return to main menu
        """)
        if not check_special_characters(manage_choice):
            manage_choice = 0
        manage_choice = int(manage_choice)
    if manage_choice == 1:
        print_all_users()
    if manage_choice == 2:
        print_all_users()
        username = input(
            """
            Type new user's username you want
            """
        )
        new_user(username, stdscr=None)
    if manage_choice == 3:
        print_all_users()
        username = input(
            """
            Type user's username who want
            """
        )
        delete_user(username)
    if manage_choice == 4:
        return "main"
    return None
