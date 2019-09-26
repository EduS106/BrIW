import os
from source.data_converter import ids_to_data
from source.data_viewer import draw_table
from source.file_handler import save_to_file
from source.data_manipulator import add_entries, remove_entries
from source.input_cleaner import number_cleaner
from source.round_object import Round


def draw_menu(menu_options, drawing="", message="Please enter the number of your selection: "):

    if drawing != "":
        print(drawing)

    for option in menu_options:
        print(f"[{option}] {menu_options[option]}")
        if option == 3 or option == 5 or option == 7 or option == 9:
            print()
    print()

    user_selection = input(message)

    if user_selection.isdigit():
        user_selection = int(user_selection)
    else:
        user_selection = 0

    return user_selection


def draw_brIW():
    return '''Welcome to BrIW v2.0 beta

                                 ____      _____        __
                                | __ ) _ _|_ _\ \      / /
                                |  _ \| '__| | \ \ /\ / / 
            /~~~~~~~~/|         | |_) | |  | |  \ V  V /  
           / /######/ / |       |____/|_| |___|  \_/\_/   
          / /______/ /  |   
         ============ /||     
         |__________|/ ||     
          |\__,,__/    ||
          | __,,__     ||
          |_\====/%____||
         /| /~~~~\ %  / |
        /_|/      \%_/  |
        | |        | | /
        |__\______/__|/

        ~~~~~~~~~~~~~~

What would you like to do? Choose from the following options:\n'''


def edit_menu(possible_options):
    prompt = f"Please enter your selection number. Number [1] to {possible_options[1]}, or [2] to {possible_options[2]}: "
    selected_option = 0
    incorrect_input = True
    while incorrect_input:
        selected_option = draw_menu(possible_options, message=prompt)
        if selected_option <= 0 or selected_option > len(possible_options):
            incorrect_input = True
            input("Please enter the number of your selection only. Press ENTER to try again.")
        else:
            incorrect_input = False

    return possible_options[selected_option]


def round_menu(menu_options, people_dict, drinks_dict, last_order_dict):

    round_instance = initialise_round(people_dict)

    if round_instance == 0:
        return

    round_instance = round_intro(round_instance, drinks_dict)

    while round_instance.active:
        os.system("clear")
        orders_dict = ids_to_data(round_instance.orders, people_dict, drinks_dict)

        draw_table("orders", orders_dict, 2)
        editing_choice = draw_menu(menu_options)

        os.system("clear")

        if editing_choice == 1:
            round_instance.orders = add_entries(round_instance.orders, "orders", people_dict, drinks_dict)

        elif editing_choice == 2:
            round_instance.orders = remove_entries(round_instance.orders, "orders", people_dict, drinks_dict)

        elif editing_choice == 3:
            final_order = round_instance.close_round()
            final_order_data = ids_to_data(final_order, people_dict, drinks_dict)
            print("The final order is:\n")
            draw_table("orders", final_order_data, 2)
            last_order_dict = final_order
            save_to_file("orders", final_order)

        else:
            input("Please enter a number from the following options. Press ENTER to try again.")

    return last_order_dict


def round_intro(round_instance, drinks_dict):
    while True:
        os.system("clear")

        ids = draw_table("drinks", drinks_dict)
        brewer_drink_id = round_instance.welcome(ids, drinks_dict)

        if brewer_drink_id == -1:
            continue
        elif brewer_drink_id == 0:
            return round_instance
        else:
            round_instance.add_order(round_instance.brewer_id, brewer_drink_id)
            return round_instance


def initialise_round(people_dict):
    while True:
        os.system("clear")
        ids = draw_table("people", people_dict)
        brewer_chosen = input('''What number is your name?    
(If it is not on the list, type X to return to main menu.)
Name Number: ''')
        if brewer_chosen.upper() == "X":
            return 0
        else:
            brewer_chosen = number_cleaner(brewer_chosen)

        if len(brewer_chosen) == 1:
            brewer_index = brewer_chosen[0] - 1
            if brewer_index < len(ids) and brewer_index != -1:
                brewer_id = ids[brewer_index]
                new_round = Round(people_dict[brewer_id], brewer_id)
                return new_round
            else:
                user_exit = input('''Please make sure your name is on the list, please exit and add it if it is not.

Press ENTER to try again or type X to exit: ''')
                if user_exit.upper() == "X":
                    return 0
        else:
            user_exit = input('''Please only enter one number. Do not include words or special characters (!@£$%%^&*).

Press ENTER to go back and try again, or type X to exit: ''')
            if user_exit.upper() == "X":
                return 0


def exit_screen():
    os.system("clear")

    exit_message = """
Thanks for using our app, hope you have enjoyed the experience!


                    *****************
               ******               ******
           ****                           ****
        ****                                 ***
      ***                                       ***
     **           ***               ***           **
   **           *******           *******          ***
  **            *******           *******            **
 **             *******           *******             **
 **               ***               ***               **
**                                                     **
**       *                                     *       **
**      **                                     **      **
 **   ****                                     ****   **
 **      **                                   **      **
  **       ***                             ***       **
   ***       ****                       ****       ***
     **         ******             ******         **
      ***            ***************            ***
        ****                                 ****
           ****                           ****
               ******               ******
                    *****************


Contact us to report bugs, for help or troubleshooting, or just to give us feedback on our app!

Email: thebriwcompany@coffee.com
Phone: 07180350283

Copyright: Eduardo Salazar, 2019"""

    print(exit_message)
    exit()