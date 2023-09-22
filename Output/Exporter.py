from Backend import DataContainer
import heapq
import pandas as pd

from Global import KEYWORD_DETERMINATION_OPTIONS, sort_dict_by_value


class Exporter:
    def __init__(self, data_container: DataContainer):
        self.data_container: DataContainer = data_container

    def company_layer(self, word_rating_type, key_word_count, in_percent):
        print_data = {
            'Company Name': [company.name for company in self.data_container.general_layer.company_stack.companies],
            'Business Description': [],
            'Description Word Count': [],
        }

        for nr in range(key_word_count):
            print_data[f"Top-{nr+1} word"] = []
            print_data[f"Top-{nr+1} word count"] = []
            nr += 1

        print("Outputting company-layer data")
        print(print_data)

    def create_word_rating(self, in_percent, word_rating_type):
        top_words = {}
        for key, value in self.data_container.general_layer.of_word.items():
            if word_rating_type == KEYWORD_DETERMINATION_OPTIONS[0]:
                top_words[key] = value.quantity.percent if in_percent else value.quantity.count
            if word_rating_type == KEYWORD_DETERMINATION_OPTIONS[1]:
                top_words[key] = value.frequency.percent if in_percent else value.frequency.count
        top_words = sort_dict_by_value(top_words)
        return top_words

    def generic_layer(self):
        # Implement logic to output generic-layer data here
        print("Outputting generic-layer data")

    def cluster_layer(self):
        # Implement logic to output cluster-layer data here
        print("Outputting cluster-layer data")

    # You can add more output methods as needed
