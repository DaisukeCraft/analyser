from pprint import pprint
from typing import Tuple
import pandas as pd


class Importer:
    BUSINESS_DESCRIPTION = 'Business Description'

    def __init__(self):
        self.loaded = False
        self.analysed = False

    def import_files(self, file_paths: Tuple[str]):
        print(type(file_paths))
        if file_paths:
            for path in file_paths:
                df = pd.read_excel(path, header=2, index_col=0).to_dict()
                if not self.BUSINESS_DESCRIPTION in df:
                    raise KeyError()

                print(df[self.BUSINESS_DESCRIPTION].keys())
            self.loaded = True

    def analyze_excel(self, file_path):
        for company_and_description in tqdm(df, desc="Analyzing data"):
            for company in company_and_description.keys():
                company_abbreviation = company[::-1].split('(')[0][::-1][:-1]
                company_name = company.split(f"({company_abbreviation})")[0].translate(
                    str.maketrans('', '', string.punctuation)).strip()
                company_description = company_and_description.get(company).translate(
                    str.maketrans('', '', string.punctuation)).replace(company_name, '').strip().lower().split()

                self.dataContainer.add_company(abbreviation=company_abbreviation, name=company_name,
                                               description=company_description)

        if self.file_loaded:
            try:
                self.dataContainer.analyse(self.excluded_words)
            except Exception as e:
                print(e)
                self.label.config(text="File(s) loaded but failed to analyse")
            else:
                self.label.config(text="File(s) loaded and analysed")
