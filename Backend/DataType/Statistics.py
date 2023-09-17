from . import Statistic
from typing import List


class Statistics:
    def __init__(self, quantity: Statistic, frequency: Statistic):
        self.quantity: Statistic = quantity
        self.frequency: Statistic = frequency

    @classmethod
    def calculate_statistic(cls, needle: str, haystack: List[str]):
        count = Statistic.calculate_count(needle, haystack)
        percent = Statistic.calculate_percent(count, haystack.__len__())

        return Statistic(
            count,
            percent
        )
