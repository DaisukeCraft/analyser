from Backend import DataContainer
import pandas as pd


class Exporter:
    def __init__(self, data_container: DataContainer):
        self.data_container: DataContainer = data_container

    def company_layer(self, key_word_count):
        print_data = {
            'Company Name': [company.name for company in self.data_container.general_layer.company_stack.companies],
            'Business Description': [],
            'Description Word Count': [],
        }

        for i in range(key_word_count):


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
