import os
import sys

def start_app():

    user_exit = False

    menu_options = {1: "List of people", 2: "List of drinks", 3: "List of people and drinks", 4: "Edit people",
                    5: "Edit drinks", 6: "Exit"}
    people_dict = start_dict("people.txt")
    drinks_dict = start_dict("drinks.txt")
    preferences_dict = {}


    while not user_exit:

        os.system("clear")

        user_selection = draw_menu(menu_options)
        user_selection = int(user_selection)
        if user_selection > 6 or user_selection <= 0:
            input("\nPlease only enter a number from the options provided. Press 'Enter' to try again.")
            continue
        elif user_selection == 1:
            draw_table("people", list(people_dict.values()))
        elif user_selection == 2:
            draw_table("drinks", list(drinks_dict.values()))
        elif user_selection == 3:
            draw_table("people and drinks", [list(people_dict.values()), list(drinks_dict.values())], 2)
        elif user_selection == 4:
            people_dict = add_data("people's names", people_dict)
        elif user_selection == 5:
            people_dict = add_data("the drinks' names", drinks_dict)
        elif user_selection == 6:
            exit_screen()

        user_exit = not user_continue()

    exit_screen()


def draw_menu(menu_options):
    #num_options = len(menu_options) #to add future functionality for a dynamic list in the message and menu_options is a string array argument
    os.system("clear")

    print("Welcome to BrIW v2.0 beta\n\nWhat would you liek to do? Choose from the following options:\n")
    for option in menu_options:
        print(f"[{option}] {menu_options[option]}")
    print()

    user_selection = input("Please enter the number of your selection: ")

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
    spacing = " "*(width - len(word)) + "\t"
    return spacing


def largest_list(list_set):
    longest_list = 0
    for list_num in range(0, len(list_set)):
        list_length = len(list_set[list_num])
        if list_length > longest_list:
            longest_list = list_length
    return longest_list


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
        title_width = find_width([title])  # requires an array input
        if data_width >= title_width:
            width = data_width
        else:
            width = title_width
        max_lengths.append(width)
    else:
        for list_num in range(0, cols):
            data_width = find_width(data[list_num])
            max_lengths.append(data_width)
    extra_space = sum(max_lengths)
    return extra_space


def draw_line(cols=1, extra_space=0):
    print("=" * (4 + 8*(cols - 1)) + "=" * extra_space)


def draw_header(title, cols=1, extra_space=0):
    draw_line(cols, extra_space)
    print(title.upper())
    draw_line(cols, extra_space)


def draw_data(data, cols=1):

    if cols == 1:
        for item in data:
            print("-->", item)
    else:
        for dataset_num in range(0, len(data)):
            for item in range(0, largest_list(data)):
                for list_num in range(0, cols):
                    if len(data[list_num]) > item:
                        spacing = separator(data, data[list_num][item])
                        print("-->", data[list_num][item], end=spacing)
                    else:
                        width = find_width(data, cols)
                        spacing = separator(data)
                        print("   ", spacing, end="")
                print()
            return


def draw_footer(cols=1, extra_space=0):
    draw_line(cols, extra_space)
    print()


def draw_table(title, data, cols=1):

    os.system("clear")

    extra_space = largest_space(data, title, cols)

    draw_header(title, cols, extra_space)

    draw_data(data, cols)

    draw_footer(cols, extra_space)


def add_data(data_name, data):

    os.system("clear")

    added_data = input(f"\nPlease enter {data_name} separated by commas: ")
    print()
    added_data = added_data.split(",")

    for item in added_data:
        item_index = added_data.index(item)
        item = item.strip()
        item = item.strip('"')
        item = item.strip("'")
        item = item.title()
        added_data[item_index] = item

    if isinstance(data, list):
        data += added_data
    elif isinstance(data, dict):
        data = update_data(data_name, added_data, data)

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
Thanks for using our app, hope you have enjoyed the experience :)
    
Contact us to report bugs, for help or troubleshooting, or just to give us feedback on our app!
    
Email: ahsc1997@gmail.com
Phone: 07803407324
    
Copyright: Eduardo Salazar, 2019"""

    print(exit_message)
    exit()


def save_to_file(data_name, data):
    if data_name == "people's names":
        file = open("people.txt", "w")
    elif data_name == "the drinks' names":
        file = open("drinks.txt", "w")
    else:
        raise Exception("Error: only supports 'people's names' (people) and 'the drinks' names' (drinks) for "
                        "data_name string literal")

    for key in data:
        file.write(str(key) + "- " + data[key] + "\n")

    file.close()


def update_data(data_name, added_data, dictionary):
    for item in added_data:
        id = 1
        while id in dictionary:
            id += 1
        new_entry = {id: item}
        dictionary.update(new_entry)
    save_to_file(data_name, dictionary)
    return dictionary





start_app()