from source.data_converter import dict_to_list


def draw_table(title, data, cols=1):

    data_list = []
    if cols == 1:
        if isinstance(data, dict):
            list_to_add = list(data.values())
        elif isinstance(data, list):
            list_to_add = data
        data_list += list_to_add
    else:
        for data_col in data:
            list_to_add = []
            if isinstance(data_col, dict):
                list_to_add = list(data_col.values())
            if isinstance(data_col, list):
                list_to_add = data_col
            data_list.append(list_to_add)

    extra_space = largest_space(data_list, title, cols)

    largest_index = len(str(largest_dict(data, cols)))

    draw_header(title, cols, extra_space, largest_index)

    ids = draw_data(data, cols, largest_index)

    draw_footer(cols, extra_space, largest_index)

    return ids


def draw_data(data, cols=1, largest_index=1):
    ids = []
    if cols == 1:
        index = 0
        for user_id, item in data.items():
            index += 1
            print(f"[{index}]\t", data[user_id])
            ids.append(user_id)
        return ids
    else:
        for dataset_num in range(0, len(data)):
            data_list = []
            if isinstance(data[dataset_num], dict):
                data_list = dict_to_list(data, 2)
                ids = list(data[0].keys())
            elif isinstance(data[dataset_num], list):
                data_list = data
                ids = "Returning ids for a list of data has not yet been implemented."

            for index in range(0, largest_dict(data, cols)):
                for dict_num in range(0, cols):
                    if len(data[dict_num]) > index:
                        spacing = separator(data_list, data_list[dict_num][index])
                        print(f"[{index + 1}]\t", data_list[dict_num][index], end=spacing+" \t")
                    else:
                        spacing = " " * find_width(data_list) + " " + "  "*cols
                        print(" "*largest_index + "\t" + spacing, end=" "*largest_index + " \t")
                print()
            return ids


def draw_line(cols=1, letter_space=0, largest_index=1):
    tabs_and_spaces = 7 * cols + 8 * (cols - 1)
    little_overhang = 2 * "="
    print("=" * tabs_and_spaces + "=" * letter_space + "==" * largest_index * cols + little_overhang)


def draw_header(title, cols=1, extra_space=0, largest_index=1):
    draw_line(cols, extra_space, largest_index)
    print(title.upper())
    draw_line(cols, extra_space, largest_index)


def draw_footer(cols=1, extra_space=0, largest_index=1):
    draw_line(cols, extra_space, largest_index)
    print()


def separator(data, word=""):
    cols = len(data)
    width = find_width(data[0:-1], cols)
    spacing = " " * (width - len(word))
    return spacing


def largest_space(data, title, cols=1):
    max_lengths = []
    if cols == 1:
        data_width = find_width(data, cols)
        max_lengths.append(data_width)
    else:
        for list_num in range(0, cols):
            data_width = find_width(data[list_num])
            max_lengths.append(data_width)
    final_width = sum(max_lengths)

    title_width = find_width([title])  # requires an array input

    if final_width >= title_width:
        letter_space = final_width
    else:
        letter_space = title_width

    return letter_space


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


def largest_dict(dict_set, cols=1):
    longest_dict = len(dict_set)
    if cols > 1:
        for dict_num in range(0, len(dict_set)):
            dict_length = len(dict_set[dict_num])
            if dict_length > longest_dict:
                longest_dict = dict_length
    return longest_dict


def draw_selected_people(people_dict, selected_people, people_ids):
    print("\n(\tPEOPLE SELECTED:\t", end="")
    for index in selected_people:
        user_id = people_ids[index - 1]
        print(f"[{index}] {people_dict[user_id]} \t", end="")
    print(")\n")