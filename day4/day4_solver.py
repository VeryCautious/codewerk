
from typing import List

from day4.game import Game


def play(games :List[Game], values :List[int]):
    for v in values:
        for game in games:
            if game.mark_value(v):
                return game.current_score() * v