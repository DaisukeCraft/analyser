from typing import List


class Description:
    def __init__(self, description: List[str]):
        self.words: List[str] = description
        self.length: int = self.length()

    def length(self) -> int:
        return len(self.words)
