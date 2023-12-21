from pathlib import Path
from typing import Dict, List

from src.Backend import DataContainer
import numpy as np
import pandas as pd

from src.Global import KEYWORD_DETERMINATION_OPTIONS


class Exporter:
    def __init__(self, data_container: DataContainer):
        self.data_container: DataContainer = data_container

    def export_company_layer(self, key_word_count, word_rating_type, in_percent):
        header = [
            ["Excluded Words:", ",".join(self.data_container.excluded_words)],
            [""],
        ]
        data = self._build_company_data(in_percent, key_word_count, word_rating_type)
        self._export_to_excel(data, header, "company_layer")

    def export_generic_layer(self, key_word_in_percent, company_in_percent):
        header = [
            ["Excluded Words:", ",".join(self.data_container.excluded_words)],
            ["Business Descriptions:", self.data_container.general_layer.company_stack.length],
            [""],
            ["* Max- oder Min-Wert, die Anzahl eines Wortes in einer Beschreibung"],
            [""],
        ]
        data = self._build_generic_data(key_word_in_percent, company_in_percent)
        self._export_to_excel(data, header, "generic_layer")

    def cluster_layer(self):
        # Implement logic to output cluster-layer data here
        print("Outputting cluster-layer data")

    def _export_to_excel(self, data: Dict[str, List], header: List[List[str]], layer_name: str):
        export_directory_name = "exports"
        Path(export_directory_name).mkdir(parents=True, exist_ok=True)

        dataframe = pd.DataFrame(data, columns=list(data.keys()))
        with pd.ExcelWriter(f"{export_directory_name}/{layer_name}.xlsx") as writer:
            pd.DataFrame(header).to_excel(writer, sheet_name="Sheet1", header=False, index=False)
            dataframe.to_excel(writer, sheet_name="Sheet1", startrow=len(header), index=False)

    def _build_company_data(self, in_percent, key_word_count, word_rating_type):
        count_print_suffix = '%' if in_percent else ''

        print_data = {
                         'Company Name': [company.name for company in
                                          self.data_container.general_layer.company_stack.companies],
                         'Company Abbreviation': [company.abbreviation for company in
                                                  self.data_container.general_layer.company_stack.companies],
                         'Business Description': [" ".join(company.description.words) for company in
                                                  self.data_container.general_layer.company_stack.companies],
                         'Description Word Count': [company.description.length for company in
                                                    self.data_container.general_layer.company_stack.companies],
                     } | self.format_rating(key_word_count=key_word_count)
        if word_rating_type == KEYWORD_DETERMINATION_OPTIONS[0]:
            word_tier_list = sorted([stat for stat in self.data_container.general_layer.of_word.items()],
                                    key=lambda item: item[1].quantity.count, reverse=True)
        else:
            word_tier_list = sorted([stat for stat in self.data_container.general_layer.of_word.items()],
                                    key=lambda item: item[1].frequency.count, reverse=True)
        for i in range(key_word_count):
            key_word = word_tier_list[i][0]

            print_data[f"Top-{i + 1} word"] = [
                key_word for x in range(len(print_data['Company Name']))
            ]

            for company in self.data_container.general_layer.company_stack.companies:

                if key_word in company.of_word:
                    word_count_string = str(
                        company.of_word[key_word].percent if in_percent else company.of_word[key_word].count
                    )
                    word_count_string += count_print_suffix

                    print_data[f"Top-{i + 1} word count"].append(word_count_string)
                else:
                    print_data[f"Top-{i + 1} word count"].append(str(0) + count_print_suffix)
        return print_data

    def _build_generic_data(self, key_word_in_percent, company_in_percent):
        key_word_print_suffix = '%' if key_word_in_percent else ''
        company_print_suffix = '%' if company_in_percent else ''

        word_tier_list = sorted([stat for stat in self.data_container.general_layer.of_word.items()],
                                key=lambda item: item[1].quantity.count, reverse=True)

        keywords = [stat[0] for stat in word_tier_list]
        count = [str(stat[1].quantity.percent) + key_word_print_suffix for stat in
                 word_tier_list] if key_word_in_percent else [stat[1].quantity.count for stat in word_tier_list]
        contained = [str(stat[1].frequency.percent) + company_print_suffix for stat in
                     word_tier_list] if company_in_percent else [stat[1].frequency.count for stat in word_tier_list]

        print_data = {
            'Keyword': keywords,
            'Percent' if key_word_in_percent else 'Count (Quantity)': count,
            'Used in Descriptions (Occurrence)': contained,
            'Max*': [max([company.of_word[word].count if word in company.of_word else 0 for company in
                          self.data_container.general_layer.company_stack.companies]) for word in keywords],
            'Min*': [min([company.of_word[word].count if word in company.of_word else 0 for company in
                          self.data_container.general_layer.company_stack.companies]) for word in keywords],
        }

        return print_data

    def format_rating(self, key_word_count):
        top_words = [f"Top-{nr + 1} word" for nr in range(key_word_count)]
        word_counts = [f"Top-{nr + 1} word count" for nr in range(key_word_count)]

        ratings = np.array([list(rating) for rating in zip(top_words, word_counts)])
        ratings = ratings.flatten()

        return {ratings[i]: [] for i in range(len(ratings))}
