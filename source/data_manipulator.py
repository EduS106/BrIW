from source.file_handler import save_to_file
from source.data_viewer import draw_table, draw_selected_people
from source.input_cleaner import name_cleaner, number_cleaner
from source.data_converter import ids_to_data
import os


def add_data(data_name, data):

    os.system("clear")

    ids = draw_table(data_name, data)

    added_data = input(f"\nPlease enter the name of the {data_name} you would like to ADD, separated by commas: ")
    print()

    added_data = name_cleaner(added_data)

    if added_data == "":
        return data

    if isinstance(data, list):
        data += added_data
    elif isinstance(data, dict):
        data = update_data(data_name, added_data, data, ids, mode="add")

    return data


def remove_data(data_name, data, preferences):

    os.system("clear")

    ids = draw_table(data_name, data)

    removed_data = input(f"\nPlease enter the number of the {data_name} you would like to REMOVE, separated by commas: ")
    print()

    removed_data = number_cleaner(removed_data)

    if isinstance(data, list):
        for item in removed_data:
            if item < len(data):
                removed_data.remove(item)
    elif isinstance(data, dict):
        data = update_data(data_name, removed_data, data, ids, mode="remove", preferences=preferences)

    return data


def update_data(data_name, input_data, dictionary, ids=[], mode="add", preferences={}):

    if mode == "add":
        dictionary = update_data_add(input_data, ids, dictionary)

    elif mode == "remove":
        dictionary = update_data_remove(data_name, input_data, ids, dictionary, preferences)

    save_to_file(data_name, dictionary)

    return dictionary


def update_data_add(input_data, ids, dictionary):
    highest_id = 0
    for item in input_data:
        if highest_id == 0:
            for user_id in ids:
                if user_id > highest_id:
                    highest_id = user_id
        if item != "":
            new_entry = {highest_id + 1: item}
            dictionary.update(new_entry)
            highest_id += 1

    return dictionary


def update_data_remove(data_name, input_data, ids, dictionary, preferences):
    for item in input_data:
        if item > len(ids):
            input_data.remove(item)
            print(f"Entry out of range. Ignored the following entries: {item}")
    for choice in input_data:
        index = choice - 1
        people = list(preferences.keys())
        drinks = list(preferences.values())
        prohibited = people if data_name == "people" else drinks
        if ids[index] in prohibited:
            print("\nERROR: One or more of your selected items cannot be removed. These have been ignored.")
            print("Please delete any items from any active preferences before attempting to delete them.")
            print("Please return to Main Menu and try again once your preferences have been amended.")
        else:
            dictionary.pop(ids[index])

    return dictionary


def add_entries(dictionary, dictionary_file, people_dict, drinks_dict):
    while True:
        os.system("clear")

        people_ids, added_people = add_entry_menu("people", people_dict)

        if len(added_people) != 0:

            draw_selected_people(people_dict, added_people, people_ids)

            drink_ids, added_drinks = add_entry_menu("drinks", drinks_dict)

            if len(added_people) == len(added_drinks):
                for index in range(0, len(added_people)):
                    people_id = people_ids[added_people[index] - 1]
                    drink_id = drink_ids[added_drinks[index] - 1]
                    dictionary.update({people_id: drink_id})

                save_to_file(dictionary_file, dictionary)
                return dictionary

            else:
                back = input("You must assign a drink for each person. Please add the same number of people as drinks. "
                             "Press ENTER to try again, or [X] to exit: ")
                back = back.strip()
                os.system("clear")
                if back.upper() == "X":
                    print()
                    return dictionary

        else:
            back = input("You must select at least 1 person. Press ENTER to try again, or [X] to exit: ")
            back = back.strip()
            os.system("clear")
            if back.upper() == "X":
                print()
                return dictionary


def add_entry_menu(data_name, dictionary):
    ids = draw_table(data_name, dictionary)

    added_data = input(
        f"\nPlease enter the numbers of the {data_name} you would like to ADD/CHANGE, separated by commas: ")
    print()

    added_data = number_cleaner(added_data)

    invalid_data = []
    for item in added_data:
        if item > len(ids):
            invalid_data.append(item)

    for invalid_entry in invalid_data:
        added_data.remove(invalid_entry)
        input(f"Entry out of range. Ignored the following entry: {invalid_entry}\n\nPress ENTER to continue.\n")

    os.system("clear")

    return ids, added_data


def remove_entries(dictionary, dictionary_name, people_dict, drinks_dict):

    os.system("clear")

    dictionary_data = ids_to_data(dictionary, people_dict, drinks_dict)
    draw_table(dictionary_name, dictionary_data, 2)
    ids = []
    for user_id in dictionary.keys():
        ids.append(user_id)

    removed_data = input(f"\nPlease enter the numbers of the people whose {dictionary_name} you would like to REMOVE, "
                         f"separated by commas: ")
    print()

    if removed_data.strip() != "" and not removed_data.isalpha():
        removed_data = number_cleaner(removed_data)
    else:
        return dictionary

    if isinstance(dictionary, list):
        for item in removed_data:
            dictionary.remove(item)
    elif isinstance(dictionary, dict):
        data = update_data("preferences", removed_data, dictionary, ids, "remove")

    return data