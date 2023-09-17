from typing import List
from Backend.Layer import Company


class Stack:
    def __init__(self, stack: List[Company]):
        self.content: List[Company] = stack
        self.length: int = self.length()

    def length(self) -> int:
        return len(self.content)
