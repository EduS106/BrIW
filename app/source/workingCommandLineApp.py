#!/Users/ehsc1997/anaconda3/bin/python3
import sys
arguments = sys.argv

people = ["Eduardo", "Conner", "John", "Julio", "Nick", "Danny", "Billy", "Connor"]
drinks = ["Coffee", "Beer", "Earl Gray Tea", "San Miguel", "Red Bull", "Protein Smoothies", "Milkshakes", "Water"]

def table_print(people_or_drinks="get-people"):
    if people_or_drinks == "get-people":
        print("------------------------------")
        print("PEOPLE")
        print("------------------------------")
        for person in people:
            print("--> ", person)
        print("------------------------------")
    elif people_or_drinks == "get-drinks":
        print("------------------------------")
        print("DRINKS")
        print("------------------------------")
        for drink in drinks:
            print("--> ", drink)
        print("------------------------------")


if len(arguments) >= 2:
    command = arguments[1]
    if command == "get-people" or command == "get-drinks":
        table_print(command)
    else:
        print("Please enter only 1 of the following arguments: 'get-people' or 'get-drinks'.")
else:
    print("Please enter only 1 argument: 'get-people' or 'get-drinks'.")
