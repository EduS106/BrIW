def number_cleaner(input_data):
    allowed_characters = [",", " "]
    input_data = ''.join([character for character in input_data if character.isdigit() or character in allowed_characters])
    input_data = input_data.split(",")
    invalid_entries = {}

    for index in range(0, len(input_data)):
        item = input_data[index]
        item = item.strip()
        item = item.strip('"')
        item = item.strip("'")
        if item != "":
            item = int(item)
            input_data[index] = item
        else:
            invalid_entries.update({index: input_data[index]})

    for invalid_index, invalid_item in invalid_entries.items():
        print(f"The following invalid entry was ignored: Entry Number {invalid_index + 1}\n")
        input_data.remove(invalid_item)

    return input_data


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