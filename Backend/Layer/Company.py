from typing import List, Optional, Dict
from Backend.Attribute import Description
from Backend.DataType import Statistic


class Company:
    def __init__(self, abbreviation: str, name: str, description: List[str]):
        self.abbreviation: str = abbreviation
        self.name: str = name
        self.description: Description = Description(description)
        self.statistics: Dict[str, Statistic] = {}

    def analyse(self, excluded_words: Optional[List[str]]) -> None:
        """Analyses statistics for every word in the description, excluding specified words"""
        for word in self.description.content:
            if word in excluded_words or word.isdigit():
                continue

            count = Statistic.calculate_count(word, self.description.content)
            percent = Statistic.calculate_percent(count, self.description.length)

            self.statistics[word] = Statistic(count, percent)
