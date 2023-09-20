from .Layer import Company, General
from typing import List, Optional


class DataContainer:
    def __init__(self, excluded_words: Optional[List[str]]):
        self.excluded_words: Optional[List[str]] = excluded_words
        self.company_stack: List[Company] = []
        self.general_layer: Optional[General] = None

    def analyse(self, excluded_words: Optional[List[str]] = None) -> None:
        if len(self.company_stack) < 1:
            raise IndexError('No data to analyse')

        self.general_layer = General(self.company_stack)
        self.general_layer.analyse(excluded_words)

    def add_company(self, abbreviation: str, name: str, description: List[str]) -> None:
        self.company_stack.append(
            Company(
                abbreviation,
                name,
                description,
            )
        )
