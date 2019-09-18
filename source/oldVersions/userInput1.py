import os
import sys

def start_app():

    # data_size = len(initial_data)
    # #(use later for dynamic data where initial_data is in the form of a dictionary and initial_data is an argument)
    user_exit = False

    people = ["Ed", "Greg", "Danny", "Dragos", "Anjali", "Ralph", "Billy", "Dan", "Eduardo", "Lydia"]
    drinks = ["Flat White", "Green Tea", "Americano", "Lemon Tea", "Black Coffee", "Iced Latte", "Yorkshire Tea", "Irish Coffee", "Scottish Coffee", "Hot Toddy", "Frapuccino", "Starbucks"]
    #user_dict = create_dict(people, drinks)

    while not user_exit:

        os.system("clear")

        user_selection = draw_menu()
        user_selection = int(user_selection)
        if user_selection > 6 or user_selection <= 0:
            input("\nPlease only enter a number from the options provided. Press 'Enter' to try again.")
            continue
        elif user_selection == 1:
            draw_table("people", people)
        elif user_selection == 2:
            draw_table("drinks", drinks)
        elif user_selection == 3:
            draw_table("people and drinks", [people, drinks], 2)
        elif user_selection == 4:
            people = add_data("people's names", people)
        elif user_selection == 5:
            drinks = add_data("the drinks' names", drinks)
        elif user_selection == 6:
            exit_screen()

        user_exit = not user_continue()

    exit_screen()


def draw_menu():
    #num_options = len(menu_options) #to add future functionality for a dynamic list in the message and menu_options is a string array argument
    os.system("clear")

    menu = """ 
Welcome to BrIW v2.0 beta
    
What would you like to do? Choose from the following options:
    
    [1] Get people
    [2] Get drinks
    [3] Get people and drinks
    [4] Add people
    [5] Add drinks
    [6] Exit
    """

    print(menu)

    user_selection = input("Please enter the number of your selection: ")

    if user_selection.isdigit():
        user_selection = int(user_selection)
    else:
        user_selection = 0

    return user_selection


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
            return largest_space


def draw_line(width=20, cols=1, extra_space=0):
    print("=" * (width + 8) * cols + "=" * extra_space * (cols - 1))


def draw_header(title, width=20, cols=1, extra_space=0):
    draw_line(width, cols, extra_space)
    print(title.upper())
    draw_line(width, cols, extra_space)


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


def draw_footer(width=20, cols=1, extra_space=0):
    draw_line(width, cols, extra_space)
    print()


def draw_table(title, data, cols=1):

    os.system("clear")

    data_width = find_width(data, cols)
    title_width = find_width([title]) # requires an array input
    extra_space = largest_space(data, cols)

    width = 20
    if data_width >= title_width:
        width = data_width
    else:
        width = title_width

    draw_header(title, width, cols, extra_space)

    draw_data(data, cols)

    draw_footer(width, cols, extra_space)


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

    data += added_data

    return data


def user_continue():

    os.system("clear")

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


'''def create_dict(data1, data2):

    user_dict = {}

    if len(data1) == len(data2):
        for i in range(0, len(data1)):
            user_dict[data1[i]] = data2[i]

    elif len(data1) > len(data2):
        for i in range(0, len(data1)):
            if i >= len(data2):
                user_dict[data1[i]] = "Americano"
            else:
                user_dict[data1[i]] = data2[i]
    else:
        for i in range(0, len(data2)):
            if i >= len(data1):
                user_dict[data2[i]] = "Unspecified"
            else:
                user_dict[data2[i]] = data1[i]

    return user_dict'''


start_app()