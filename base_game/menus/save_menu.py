from base_game.utils import check_special_characters


def saves_menu():
    """
    Display saves' manager menu and execute function with user's choice  or return to main menu
    :return: int
    """
    manage_choice = 0
    while (
            manage_choice != 1
            and manage_choice != 2
            and manage_choice != 3
    ):
        manage_choice = input("""
        [1] - Display saves list      
        [2] - Delete a save
        [3] - return to main menu
        """)
        if not check_special_characters(manage_choice):
            manage_choice = 0
        manage_choice = int(manage_choice)
    if manage_choice == 1:
        pass
        # print_all_saves()
    if manage_choice == 2:
        pass
        # print_all_saves()
    if manage_choice == 3:
        return "main"
    return None
