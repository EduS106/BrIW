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