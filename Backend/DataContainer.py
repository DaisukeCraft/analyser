from .Layer import Company, General
from typing import List, Optional


class DataContainer:
    def __init__(self):
        self.stack: List[Company] = []
        self.data: Optional[General] = None

    def analyse(self, excluded_words: Optional[List[str]] = None) -> None:
        if len(self.stack) < 1:
            return

        self.data = General(self.stack)
        self.data.analyse(excluded_words)

    def add_company(self, abbreviation: str, name: str, description: List[str]) -> None:
        self.stack.append(
            Company(
                abbreviation,
                name,
                description,
            )
        )
