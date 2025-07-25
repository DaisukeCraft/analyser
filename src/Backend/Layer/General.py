from functools import reduce
from typing import List, Optional, Dict
from src.Backend.DataType import Statistics, Statistic
from src.Backend.Attribute import Stack
from src.Backend.Layer import Company


class General:
    def __init__(self, stack: List[Company]):
        self.company_stack: Stack = Stack(stack)
        self.of_word: Dict[str, Statistics] = {}

    def analyse(self, excluded_words: Optional[List[str]]) -> None:
        """Populates data for every word in the companies descriptions, excluding specified words"""
        for company in self.company_stack.companies:
            if not company.of_word:
                company.analyse(excluded_words)

            for word, stats in company.of_word.items():
                if word not in self.of_word:
                    self.of_word[word] = Statistics(
                        Statistic(None, None),
                        Statistic(None, None)
                    )

                self.of_word[word].quantity.count += stats.count
                self.of_word[word].frequency.count += 1

        total_description_length = reduce(
            lambda x, y: x + y,
            [company.description.length for company in self.company_stack.companies]
        )
        total_stack_size = self.company_stack.length

        for word in self.of_word:
            self.of_word[word].quantity.percent = Statistic.calculate_percent(
                self.of_word[word].quantity.count,
                total_description_length
            )

            self.of_word[word].frequency.percent = Statistic.calculate_percent(
                self.of_word[word].frequency.count,
                total_stack_size
            )

        self.exclude_irrelevant_words()

    def exclude_irrelevant_words(self):
        to_be_deleted = []
        for word, value in self.of_word.items():
            if value.frequency.percent >= 100:
                to_be_deleted.append(word)

        for word in to_be_deleted:
            del self.of_word[word]
