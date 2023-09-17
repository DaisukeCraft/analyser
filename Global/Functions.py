def sort_dict_by_key(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[0]))


def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
