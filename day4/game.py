
from typing import Dict, List, Tuple


class Game:

    lookup : Dict[int, Tuple[int, int]]
    score: Dict[str, int]
    values: List[int]
    
    def __init__(self, board):
        lookup = dict()
        items = [(int(board[y][x]), (y, x)) for x in range(5) for y in range(5)]
        lookup.update(items)
        self.lookup = lookup

        score = dict()
        self.score = score

        self.values = [int(board[y][x]) for x in range(5) for y in range(5)]

    def current_score(self) -> int:
        return sum(self.values)

    def mark_value(self, value: int) -> bool:
        if not  value in self.lookup:
            return False

        (y, x) = self.lookup[value]
        self.values.remove(value)

        xKey = 'x' + str(x)
        yKey = 'y' + str(y)
        
        self.score.setdefault(xKey, 0)
        self.score.setdefault(yKey, 0)

        self.score[xKey] += 1
        self.score[yKey] += 1

        return self.score[xKey] >= 5 or self.score[yKey] >= 5