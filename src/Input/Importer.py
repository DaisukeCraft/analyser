from src.Backend import DataContainer
from typing import Tuple
import pandas as pd
import string


class Importer:
    BUSINESS_DESCRIPTION = 'Business Description'
    COMPANY_NAME = 'Company Name'

    def __init__(self, data_container: DataContainer):
        self.dataContainer: DataContainer = data_container

    def import_files(self, file_paths: Tuple[str]):
        if not file_paths:
            raise FileNotFoundError("No file selected")

        for path in file_paths:
            data = pd.read_excel(path, header=0, index_col=0).to_dict()
            if self.BUSINESS_DESCRIPTION not in data:
                raise KeyError("Wrong file format")

            self.extract_companies(data[self.BUSINESS_DESCRIPTION])

    def extract_companies(self, data: dict):
        for data_key, data_set in data.items():
            abbreviation = data_key[::-1].split('(')[0][::-1][:-1]
            name = data_key.split(
                f"({abbreviation})"
            )[0].translate(
                str.maketrans(
                    '',
                    '',
                    string.punctuation
                )
            ).strip()
            description = data_set.translate(
                str.maketrans(
                    '',
                    '',
                    string.punctuation
                )
            ).replace(
                name,
                ''
            ).strip().lower().split()

            self.dataContainer.add_company(abbreviation, name, description)
