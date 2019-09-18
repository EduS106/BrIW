import sys
arguments = sys.argv

people = ["Eduardo", "Conner", "John", "Julio", "Nick", "Danny", "Billy", "Connor"]
drinks = ["Coffee", "Beer", "Earl Gray Tea", "San Miguel", "Red Bull", "Protein Smoothies", "Milkshakes", "Water"]

if len(arguments) == 2:
    command = arguments[1]
    if command == "get-people":
        print(people)
    elif command == "get-drinks":
        print(drinks)
    else:
        print("Please enter only 1 of the following arguments: 'get-people' or 'get-drinks'.")
else:
    print("Please enter only 1 argument: 'get-people' or 'get-drinks'.")