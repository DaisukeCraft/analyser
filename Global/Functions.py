def sort_dict_by_key(dictionary, key=lambda item: item[0]):
    return dict(sorted(dictionary.items(), key=key))


def sort_dict_by_value(dictionary, key=lambda item: item[1]):
    return dict(sorted(dictionary.items(), key=key, reverse=True))
