from typing import List
from src.Backend.Layer import Company


class Stack:
    def __init__(self, stack: List[Company]):
        self.companies: List[Company] = stack
        self.length: int = self.length()

    def length(self) -> int:
        return len(self.companies)
