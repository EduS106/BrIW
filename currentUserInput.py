#!/Users/ehsc1997/anaconda3/bin/python3
import os
import sys


def start_app():

    user_exit = False

    menu_options = {1: "List of people", 2: "List of drinks", 3: "List of people and drinks", 4: "Edit people",
                    5: "Edit drinks", 6: "List of preferences", 7: "Edit preferences", 8: "Exit"}

    people_dict = start_dict("people.txt")
    drinks_dict = start_dict("drinks.txt")
    preferences_dict = start_dict("preferences.txt")

    while not user_exit:

        os.system("clear")

        user_selection = draw_menu(menu_options, draw_brIW())
        user_selection = int(user_selection)
        if user_selection > len(menu_options) or user_selection <= 0:
            input("\nPlease only enter a number from the options provided. Press 'Enter' to try again.")
            continue

        elif user_selection == 1:
            draw_table("people", people_dict)

        elif user_selection == 2:
            draw_table("drinks", drinks_dict)

        elif user_selection == 3:
            draw_table("people and drinks", [people_dict, drinks_dict], 2)

        elif user_selection == 4:
            ids = draw_table("people", people_dict)
            editing_choice = edit_menu()
            if editing_choice == "ADD":
                people_dict = add_data("people", people_dict)
            elif editing_choice == "REMOVE":
                people_dict = remove_data("people", people_dict, ids)

        elif user_selection == 5:
            ids = draw_table("drinks", drinks_dict)
            editing_choice = edit_menu()
            if editing_choice == "ADD":
                drinks_dict = add_data("drinks", drinks_dict)
            elif editing_choice == "REMOVE":
                drinks_dict = remove_data("drinks", drinks_dict, ids)

        elif user_selection == 6:
            #TODO: preferences_to_list function
            draw_table("preferences", preferences_dict, 2)

        elif user_selection == 7:
            draw_table("preferences", preferences_dict, 2)
            if editing_choice == "ADD":
                drinks_dict = add_data("drinks", drinks_dict)
            elif editing_choice == "REMOVE":
                drinks_dict = remove_data("drinks", drinks_dict, ids)

        elif user_selection == 8:
            exit_screen()

        user_exit = not user_continue()

    exit_screen()


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


def draw_menu(menu_options, drawing="", message="Please enter the number of your selection: "):
    # num_options = len(menu_options) #to add future functionality for a dynamic list in the message and menu_options
    # is a string array argument

    if drawing != "":
        print(drawing)

    for option in menu_options:
        print(f"[{option}] {menu_options[option]}")
        if option == 3 or option == 5 or option == 7:
            print()
    print()

    user_selection = input(message)

    if user_selection.isdigit():
        user_selection = int(user_selection)
    else:
        user_selection = 0

    return user_selection


def start_dict(filename):
    dictionary = {}
    file = open(filename, "r")
    for item in file.readlines():
        print("Line in text file:", item)
        item = item.strip("\n")
        item = item.split("- ")
        print("List from text:", item)
        if item[0].isdigit():
            item[0] = int(item[0])
        dictionary.update({item[0]: item[1]})
    file.close()
    return dictionary


def find_width(data, cols=1):

    largest_item = 0

    if cols == 1:
        for item in data:
            item_size = len(item)
            if item_size > largest_item:
                largest_item = item_size
    else:
        for data_list in data:
            for item in data_list:
                item_size = len(item)
                if item_size > largest_item:
                    largest_item = item_size

    return largest_item


def separator(data, word=""):
    cols = len(data)
    width = find_width(data[0:-1], cols)
    spacing = " "*(width - len(word))
    return spacing


def largest_dict(dict_set, cols=1):
    longest_dict = len(dict_set)
    if cols > 1:
        for dict_num in range(0, len(dict_set)):
            dict_length = len(dict_set[dict_num])
            if dict_length > longest_dict:
                longest_dict = dict_length
    return longest_dict


'''
def largest_space(data, cols=1):
    if cols == 1:
        return 0
    else:
        for dataset_num in range(0, len(data)):
            largest_space = 0
            for list_num in range(0, len(data[dataset_num])):
                for item in range(0, cols):
                    if len(data[item]) > list_num:
                        spacing = separator(data, data[item][list_num])
                        if len(spacing) > largest_space:
                            largest_space = len(spacing)
            return largest_space'''


def largest_space(data, title, cols=1):
    max_lengths = []
    if cols == 1:
        data_width = find_width(data, cols)
        max_lengths.append(data_width)
    else:
        for list_num in range(0, cols):
            data_width = find_width(data[list_num])
            max_lengths.append(data_width)
    final_width = sum(max_lengths)

    title_width = find_width([title])  # requires an array input

    if final_width >= title_width:
        letter_space = final_width
    else:
        letter_space = title_width

    return letter_space


def draw_line(cols=1, letter_space=0, largest_index=1):
    tabs_and_spaces = 7 * cols + 8 * (cols - 1)
    little_overhang = 2 * "="
    print("=" * tabs_and_spaces + "=" * letter_space + "==" * largest_index * cols + little_overhang)


def draw_header(title, cols=1, extra_space=0, largest_index=1):
    draw_line(cols, extra_space, largest_index)
    print(title.upper())
    draw_line(cols, extra_space, largest_index)


def draw_data(data, cols=1, largest_index=1):
    ids = []
    if cols == 1:
        index = 0
        for user_id, item in data.items():
            index += 1
            print(f"[{index}]\t", data[user_id])
            ids.append(user_id)
        return ids
    else:
        ids = "Implementation returning ids is incomplete: draw_data only implemented to return set of ids for " \
              "single-column data "
        for dataset_num in range(0, len(data)):
            data_list = dict_to_list(data, 2)
            for index in range(0, largest_dict(data, cols)):
                for dict_num in range(0, cols):
                    if len(data[dict_num]) > index:
                        spacing = separator(data_list, data_list[dict_num][index])
                        print(f"[{index + 1}]\t", data_list[dict_num][index], end=spacing+"\t")
                    else:
                        spacing = " " * find_width(data_list)
                        print(" "*largest_index + " " + spacing, end=" "*largest_index + " ")
                print()
            return ids


'''def draw_preferences(data, cols=1):
    if cols == 1:
        for item in data:
            print(f"[{item}]", data[item])
    else:
        for dataset_num in range(0, len(data)):
            for id in range(0, largest_dict(data)):
                for dict_num in range(0, cols):
                    if len(data[dict_num]) > id:
                        print(data[dict_num][id])
                        spacing = separator(data, data[dict_num][id])
                        print(f"[{id}]", data[dict_num][id], end=spacing)
                    else:
                        width = find_width(data, cols)
                        spacing = separator(data)
                        print("   ", spacing, end="")
                print()
            return
'''


def draw_footer(cols=1, extra_space=0, largest_index=1):
    draw_line(cols, extra_space, largest_index)
    print()


def dict_to_list(data, cols=1):
    data_list = []
    if cols == 1:
        data_list += list(data.values())
    else:
        for dictionary in data:
            data_list.append(list(dictionary.values()))
    return data_list


def draw_table(title, data, cols=1):

    os.system('clear')

    data_list = []
    if cols == 1:
        data_list += list(data.values())
    else:
        for dictionary in data:
            data_list.append(list(dictionary.values()))

    extra_space = largest_space(data_list, title, cols)

    largest_index = len(str(largest_dict(data, cols)))

    draw_header(title, cols, extra_space, largest_index)

    ids = draw_data(data, cols, largest_index)

    draw_footer(cols, extra_space, largest_index)

    return ids


def name_cleaner(input_data):

    allowed_characters = [",", " ", "-"]
    input_data = ''.join([character for character in input_data if character.isalpha() or character in allowed_characters])
    input_data = input_data.split(",")

    for index in range(0, len(input_data)):
        item = input_data[index]
        item = item.strip()
        item = item.strip('"')
        item = item.strip("'")
        item = item.title()
        input_data[index] = item

    return input_data


def number_cleaner(input_data):

    allowed_characters = [",", " "]
    input_data = ''.join([character for character in input_data if character.isdigit() or character in allowed_characters])
    input_data = input_data.split(",")

    for index in range(0, len(input_data)):
        item = input_data[index]
        item = item.strip()
        item = item.strip('"')
        item = item.strip("'")
        item = int(item)
        input_data[index] = item

    return input_data


def add_data(data_name, data):

    os.system("clear")

    draw_table(data_name, data)

    added_data = input(f"\nPlease enter the name of the {data_name} you would like to add, separated by commas: ")
    print()
    added_data = name_cleaner(added_data)

    if isinstance(data, list):
        data += added_data
    elif isinstance(data, dict):
        data = update_data(data_name, added_data, data, mode="add")

    return data


def remove_data(data_name, data, ids):

    os.system("clear")

    draw_table(data_name, data)

    removed_data = input(f"\nPlease enter the number of the {data_name} you would like to remove, separated by commas: ")
    print()
    removed_data = number_cleaner(removed_data)

    if isinstance(data, list):
        for item in removed_data:
            data.remove(item)
    elif isinstance(data, dict):
        data = update_data(data_name, removed_data, data, ids, mode="remove")

    return data


def user_continue():
    keep_going = True
    user_response = input("Would you like to do something else?\nY/N: ")
    user_response = user_response.upper()
    if user_response == "N" or user_response == "NO":
        keep_going = False
    return keep_going


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
    
Email: ahsc1997@gmail.com
Phone: 07803407324
    
Copyright: Eduardo Salazar, 2019"""

    print(exit_message)
    exit()


def save_to_file(data_name, data):
    if data_name == "people":
        file = open("people.txt", "w")
    elif data_name == "drinks":
        file = open("drinks.txt", "w")
    else:
        raise Exception("Error: only supports 'people' and 'drinks' for data_name string literal")

    for key in data:
        file.write(str(key) + "- " + data[key] + "\n")

    file.close()


def update_data(data_name, input_data, dictionary, ids=[], mode="add"):
    highest_id = 0
    if mode == "add":
        for item in input_data:
            ids = list(dictionary.keys())
            if highest_id == 0:
                for user_id in ids:
                    if user_id > highest_id:
                        highest_id = user_id
            new_entry = {highest_id+1: item}
            dictionary.update(new_entry)
            highest_id += 1
    elif mode == "remove":
        for choice in input_data:
            index = choice - 1
            dictionary.pop(ids[index])

    save_to_file(data_name, dictionary)
    return dictionary


def edit_menu():
    possible_options = {1: "ADD", 2: "REMOVE"}
    prompt = "Please enter your selection number. Number [1] to ADD, or [2] to REMOVE: "
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

start_app()