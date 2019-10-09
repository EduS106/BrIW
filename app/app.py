import os
from app.source.db_extraction import table_to_dict
from app.source.data_viewer import draw_table
from app.source.menus import draw_menu, draw_brIW, edit_menu, round_menu, exit_screen
from app.source.data_manipulator import add_data, remove_data, add_entries, remove_entries
from app.source.data_converter import ids_to_data


def start_app():

    user_exit = False

    menu_options = {1: "List of people", 2: "List of drinks", 3: "List of people and drinks", 4: "Edit people",
                    5: "Edit drinks", 6: "List of preferences", 7: "Edit preferences", 8: "Start round",
                    9: "View last round", 10: "Exit"}

    edit_list_options = {1: "ADD", 2: "REMOVE"}

    edit_preferences_options = {1: "ADD/CHANGE", 2: "REMOVE"}

    edit_round_options = {1: "ADD/CHANGE", 2: "REMOVE", 3: "COMPLETE"}

    people_dict = table_to_dict("person")
    drinks_dict = table_to_dict("drink")
    preferences_dict = table_to_dict("preference")
    last_order_dict = table_to_dict("orders")

    while not user_exit:

        os.system("clear")

        user_selection = draw_menu(menu_options, draw_brIW())
        user_selection = int(user_selection)

        if user_selection > len(menu_options) or user_selection <= 0:
            input("\nPlease only enter a number from the options provided. Press 'Enter' to try again.")
            continue

        elif user_selection == 1:
            people_dict = table_to_dict("person")
            os.system("clear")
            draw_table("people", people_dict)

        elif user_selection == 2:
            drinks_dict = table_to_dict("drink")
            os.system("clear")
            draw_table("drinks", drinks_dict)

        elif user_selection == 3:
            people_dict = table_to_dict("person")
            drinks_dict = table_to_dict("drink")
            os.system("clear")
            draw_table("people and drinks", [people_dict, drinks_dict], 2)

        elif user_selection == 4:
            os.system("clear")
            draw_table("people", people_dict)
            editing_choice = edit_menu(edit_list_options)
            if editing_choice == "ADD":
                people_dict = add_data("person", people_dict)
            elif editing_choice == "REMOVE":
                people_dict = remove_data("person", people_dict)

        elif user_selection == 5:
            os.system("clear")
            draw_table("drinks", drinks_dict)
            editing_choice = edit_menu(edit_list_options)
            if editing_choice == "ADD":
                drinks_dict = add_data("drink", drinks_dict)
            elif editing_choice == "REMOVE":
                drinks_dict = remove_data("drink", drinks_dict)

        elif user_selection == 6:
            preferences_dict = table_to_dict("preference")
            os.system("clear")
            preferences_data = ids_to_data(preferences_dict, people_dict, drinks_dict)
            draw_table("preferences", preferences_data, 2)

        elif user_selection == 7:
            os.system("clear")
            preferences_data = ids_to_data(preferences_dict, people_dict, drinks_dict)
            draw_table("preferences", preferences_data, 2)
            editing_choice = edit_menu(edit_preferences_options)
            if editing_choice == "ADD/CHANGE":
                preferences_dict = add_entries(preferences_dict, "preferences", people_dict, drinks_dict)
            elif editing_choice == "REMOVE":
                preferences_dict = remove_entries(preferences_dict, "preferences", people_dict, drinks_dict)

        elif user_selection == 8:
            os.system("clear")
            last_order_dict = round_menu(edit_round_options, people_dict, drinks_dict, last_order_dict)

        elif user_selection == 9:
            last_order_dict = table_to_dict("orders")
            os.system("clear")
            last_order_data = ids_to_data(last_order_dict, people_dict, drinks_dict)
            draw_table("orders", last_order_data, 2)

        elif user_selection == 10:
            exit_screen()
            user_exit = True

        if user_selection != 10:
            input("Press ENTER to return to the Main Menu.")


if __name__ == "__main__":
    start_app()
