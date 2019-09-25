def start_dict(filename):
    dictionary = {}
    try:
        file = open(filename, "r")
    except FileNotFoundError as e:
        print("Error found:", e, ".\nCreating new file...")
        file = open(filename, "w+")

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


def save_to_file(data_name, data):
    if data_name == "people":
        file = open("data/people.txt", "w")
    elif data_name == "drinks":
        file = open("data/drinks.txt", "w")
    elif data_name == "preferences":
        file = open("data/preferences.txt", "w")
    elif data_name == "orders":
        file = open("data/last_order.txt", "w")
    else:
        print("File not found.\nCreating new file...")
        file = open(data_name, "w")

    for key in data:
        file.write(str(key) + "- " + str(data[key]) + "\n")

    file.close()