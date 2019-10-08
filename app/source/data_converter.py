def ids_to_data(dictionary, people_dict, drinks_dict):
    drink_data = []
    user_data = []

    for user_id, drink_id in dictionary.items():
        # Could add an exception if drink_id or user_id doesn't match any current value
        drink_data.append(drinks_dict[drink_id])
        user_data.append(people_dict[user_id])
    dictionary_data = [user_data, drink_data]

    return dictionary_data


def dict_to_list(data, cols=1):
    data_list = []
    if cols == 1:
        data_list += list(data.values())
    else:
        for dictionary in data:
            data_list.append(list(dictionary.values()))
    return data_list
