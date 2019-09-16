#!/Users/ehsc1997/anaconda3/bin/python3
import os
import sys


def start_app():

    user_exit = False

    menu_options = {1: "List of people", 2: "List of drinks", 3: "List of people and drinks", 4: "Edit people",
                    5: "Edit drinks", 6: "List of preferences", 7: "Edit preferences", 8: "Exit"}
    edit_list_options = {1: "ADD", 2: "REMOVE"}
    edit_preferences_options = {1: "ADD/CHANGE", 2: "REMOVE"}
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
            editing_choice = edit_menu(edit_list_options)
            if editing_choice == "ADD":
                people_dict = add_data("people", people_dict)
            elif editing_choice == "REMOVE":
                people_dict = remove_data("people", people_dict, ids, preferences=preferences_dict)

        elif user_selection == 5:
            ids = draw_table("drinks", drinks_dict)
            editing_choice = edit_menu(edit_list_options)
            if editing_choice == "ADD":
                drinks_dict = add_data("drinks", drinks_dict)
            elif editing_choice == "REMOVE":
                drinks_dict = remove_data("drinks", drinks_dict, ids, preferences=preferences_dict)

        elif user_selection == 6:
            preferences_data = ids_to_data(preferences_dict, people_dict, drinks_dict)
            draw_table("preferences", preferences_data, 2)

        elif user_selection == 7:
            preferences_data = ids_to_data(preferences_dict, people_dict, drinks_dict)
            draw_table("preferences", preferences_data, 2)
            editing_choice = edit_menu(edit_preferences_options)
            if editing_choice == "ADD/CHANGE":
                preferences_dict = add_preferences(preferences_dict, people_dict, drinks_dict)
            elif editing_choice == "REMOVE":
                preferences_dict = remove_preferences(preferences_dict, people_dict, drinks_dict)

        elif user_selection == 8:
            exit_screen()
            user_exit = True

        if user_selection != 8:
            input("Press ENTER to return to the Main Menu.")




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
        item = item.strip("\n")
        item = item.split("- ")
        if item[0].isdigit():
            item[0] = int(item[0])
        if item[1].isdigit():
            item[1] = int(item[1])
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
        for dataset_num in range(0, len(data)):
            if isinstance(data[dataset_num], dict):
                data_list = dict_to_list(data, 2)
                ids = list(data[0].keys())
            elif isinstance(data[dataset_num], list):
                data_list = data
                ids = "Returning ids for a list of data has not yet been implemented."

            for index in range(0, largest_dict(data, cols)):
                for dict_num in range(0, cols):
                    if len(data[dict_num]) > index:
                        spacing = separator(data_list, data_list[dict_num][index])
                        print(f"[{index + 1}]\t", data_list[dict_num][index], end=spacing+"\t")
                    else:
                        spacing = " " * find_width(data_list) + " " + "  "*cols
                        print(" "*largest_index  + "\t" + spacing, end=" "*largest_index + " ")
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
        if isinstance(data, dict):
            list_to_add = list(data.values())
        elif isinstance(data, list):
            list_to_add = data
        data_list += list_to_add
    else:
        for data_col in data:
            if isinstance(data_col, dict):
                list_to_add = list(data_col.values())
            if isinstance(data_col, list):
                list_to_add = data_col
            data_list.append(list_to_add)

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

    ids = draw_table(data_name, data)

    added_data = input(f"\nPlease enter the name of the {data_name} you would like to add, separated by commas: ")
    print()
    if added_data.strip() != "" and not added_data.isdigit():
        added_data = name_cleaner(added_data)
    else:
        return data

    if isinstance(data, list):
        data += added_data
    elif isinstance(data, dict):
        data = update_data(data_name, added_data, data, ids, mode="add")

    return data


def remove_data(data_name, data, ids, preferences):

    os.system("clear")

    ids = draw_table(data_name, data)

    removed_data = input(f"\nPlease enter the number of the {data_name} you would like to remove, separated by commas: ")
    print()

    if removed_data.strip() != "" and not removed_data.isalpha():
        removed_data = number_cleaner(removed_data)
    else:
        return data

    if isinstance(data, list):
        for item in removed_data:
            data.remove(item)
            if item in preferences:
                preferences.remove(item)
    elif isinstance(data, dict):
        data = update_data(data_name, removed_data, data, ids, mode="remove", preferences=preferences)

    return data


def add_preferences(preferences, people_dict, drinks_dict):

    os.system("clear")

    while True:
        people_ids = draw_table("people", people_dict)
        added_people = input(f"\nPlease enter the numbers of the people you would like to add, separated by commas: ")
        print()
        if added_people.strip() != "" and not added_people.isalpha():
            added_people = number_cleaner(added_people)
        else:
            return preferences

        drink_ids = draw_table("drinks", drinks_dict)
        print("(\tPEOPLE SELECTED:\t", end="")
        for index in added_people:
            user_id = people_ids[index - 1]
            print(f"[{index}] {people_dict[user_id]}\t", end="")
        print(")")
        added_drinks = input(f"\nPlease enter the numbers of the drinks you would like to assign to each person, "
                             f"separated by commas: ")
        print()
        if added_drinks.strip() != "" and not added_drinks.isalpha():
            added_drinks = number_cleaner(added_drinks)
        else:
            return preferences

        if len(added_people) == len(added_drinks):
            for index in range(0, len(added_people)):
                people_id = people_ids[added_people[index] - 1]
                drink_id = drink_ids[added_drinks[index] - 1]
                preferences.update({people_id: drink_id})

            save_to_file("preferences", preferences)
            return preferences

        else:
            back = input("You must assign a drink for each person. Please add the same number of people as drinks. "
                         "Press ENTER to try again, or [X] to exit: ")
            back = back.strip()
            if back.upper() == "X":
                return preferences

        # check whether adding a person who's already in the list would break or just overwrite


def remove_preferences(preferences, people_dict, drinks_dict):

    os.system("clear")

    preferences_data = ids_to_data(preferences, people_dict, drinks_dict)
    draw_table("preferences", preferences_data, 2)
    ids = []
    for user_id in preferences.keys():
        ids.append(user_id)

    removed_data = input(f"\nPlease enter the numbers of the people whose preference you would like to remove, "
                         f"separated by commas: ")
    print()
    if removed_data.strip() != "" and not removed_data.isalpha():
        removed_data = number_cleaner(removed_data)
    else:
        return preferences

    if isinstance(preferences, list):
        for item in removed_data:
            preferences.remove(item)
    elif isinstance(preferences, dict):
        data = update_data("preferences", removed_data, preferences, ids, "remove")

    return data


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
    elif data_name == "preferences":
        file = open("preferences.txt", "w")
    else:
        raise Exception("Error: only supports 'people', 'drinks' and 'preference' for data_name string literal")

    for key in data:
        file.write(str(key) + "- " + str(data[key]) + "\n")

    file.close()


def update_data(data_name, input_data, dictionary, ids=[], mode="add", preferences={}):
    highest_id = 0
    if mode == "add":
        for item in input_data:
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
            people = list(preferences.keys())
            drinks = list(preferences.values())
            prohibited = list(preferences.keys()) if data_name == "people" else list(preferences.values())
            if ids[index] in prohibited:
                print("ERROR: One or more of your selected items cannot be removed.\n")
                print("Please delete any items from any active preferences before attempting to delete them.\n")
                print("Please return to Main Menu and try again once your preferences have been amended.\n")
                return dictionary
            dictionary.pop(ids[index])

    save_to_file(data_name, dictionary)

    return dictionary


'''def update_preferences(preferences_dict, added_people, added_drinks, mode="add"):
    if mode == "add":
        for person in added_people:
            if highest_id == 0:
                for user_id in ids:
                    if user_id > highest_id:
                        highest_id = user_id
            new_entry = {highest_id+1: item}
            preferences_dict.update(new_entry)
            highest_id += 1
    elif mode == "remove":
        for choice in input_data:
            index = choice - 1
            preferences_dict.pop(ids[index])

    save_to_file("preferences", preferences_dict)
    return preferences_dict'''


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


def ids_to_data(preferences_dict, people_dict, drinks_dict):
    drink_data = []
    user_data = []

    for user_id, drink_id in preferences_dict.items():
        # Could add an exception if drink_id or user_id doesn't match any current value
        drink_data.append(drinks_dict[drink_id])
        user_data.append(people_dict[user_id])
    preference_data = [user_data, drink_data]

    return preference_data


start_app()