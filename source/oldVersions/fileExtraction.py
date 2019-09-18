def start_dict(filename):
    dictionary = {}
    file = open(filename, "r")
    for item in file.readlines():
        item = item.strip("\n")
        item = item.split("- ")
        item[0] = int(item[0])
        dictionary.update([tuple(item)])
    file.close()
    return dictionary

people = start_dict("people.txt")
drinks = start_dict("drinks.txt")
print(people, "\n", drinks, "\n")