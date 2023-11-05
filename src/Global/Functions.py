def sort_dict_by_key(dictionary, key=lambda item: item[0]):
    return dict(sorted(dictionary.items(), key=key))


def sort_dict_by_value(dictionary, key=lambda item: item[1]):
    return dict(sorted(dictionary.items(), key=key, reverse=True))


def validate_int_input(char, entry_value):
    return char.isdigit() or char == ""
