from Backend import DataContainer
import heapq
import pandas as pd

from Frontend import GUI


class Exporter:
    def __init__(self, data_container: DataContainer):
        self.data_container: DataContainer = data_container

    def company_layer(self, word_rating_type, key_word_count, in_percent):
        print_data = {
            'Company Name': [company.name for company in self.data_container.general_layer.company_stack.companies],
            'Business Description': [],
            'Description Word Count': [],
        }

        print(word_rating_type)

        if word_rating_type == GUI.KEYWORD_DETERMINATION_OPTIONS[0]:
            top_words = sorted(
                {key: value.quantity.percent if in_percent else value.quantity.count for key, value in
                 self.data_container.general_layer.of_word}
            )[:key_word_count]

        if word_rating_type == GUI.KEYWORD_DETERMINATION_OPTIONS[1]:
            top_words = sorted(
                {key: value.frequency.percent if in_percent else value.frequency.count for key, value in
                 self.data_container.general_layer.of_word}
            )[:key_word_count]

        for i in range(key_word_count):


            print(type(top_words))

            print_data[f"Top word {i}"] = top_words
            print_data[f"Top {i} count"] = self.data_container.general_layer.of_word[top_words]

        df = pd.DataFrame({
            "Excluded Words:": [','.join(self.data_container.excluded_words)],
        })
        excluded_words = pd.Series("Excluded Words:", self.data_container.excluded_words)
        head = pd.Series(["Company Name", "Business Description", "Description Word Count"])
        # Implement logic to output company-layer data here
        print("Outputting company-layer data")
        print(print_data)

    def generic_layer(self):
        # Implement logic to output generic-layer data here
        print("Outputting generic-layer data")

    def cluster_layer(self):
        # Implement logic to output cluster-layer data here
        print("Outputting cluster-layer data")

    # You can add more output methods as needed
