from functools import reduce
from typing import List, Optional, Dict
from Backend.DataType import *
from Backend.Attribute import Stack
from Backend.Layer import Company


class General:
    def __init__(self, stack: List[Company]):
        self.content: Stack = Stack(stack)
        self.statistics: Dict[str, Statistics] = {}

    def analyse(self, excluded_words: Optional[List[str]]) -> None:
        """Populates data for every word in the companies descriptions, excluding specified words"""
        for company in self.content.content:
            if not company.statistics:
                company.analyse(excluded_words)

            for word, stats in company.statistics.items():
                self.statistics[word] = Statistics(
                    Statistic(None, None),
                    Statistic(None, None)
                )

                self.statistics[word].quantity.count += stats.count
                self.statistics[word].frequency.count += 1

        total_description_length = reduce(
            lambda x, y: x + y,
            [company.description.length for company in self.content.content]
        )
        total_stack_size = self.content.length

        for word in self.statistics:
            self.statistics[word].quantity.percent = Statistic.calculate_percent(
                self.statistics[word].quantity.count,
                total_description_length
            )

            self.statistics[word].frequency.percent = Statistic.calculate_percent(
                self.statistics[word].frequency.count,
                total_stack_size
            )
