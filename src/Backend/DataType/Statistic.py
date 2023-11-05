from typing import List, Optional


class Statistic:
    def __init__(self, count: Optional[int], percent: Optional[float]):
        self.count: int = int(count or 0)
        self.percent: float = float(percent or 0)

    @classmethod
    def calculate_count(cls, needle: str, haystack: List[str]):
        return haystack.count(needle)

    @classmethod
    def calculate_percent(cls, amount: int, total: int):
        return round(float(amount / total) * 100, ndigits=2)
