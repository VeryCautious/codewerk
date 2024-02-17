
directions = {
  "forward": (1, 0),
  "down": (0, 1),
  "up": (0, -1)
}

class Submarine:
    _depth: int
    _pos: int

    def __init__(self, startDepth: int, startPos: int):
        self._depth = startDepth
        self._pos = startPos
    
    def move(self, cmd: str):
        dir, amount = cmd.split(' ')
        dPos, dDepth = directions[dir]
        self._pos += dPos * int(amount)
        self._depth += dDepth * int(amount)

    def get_location(self):
        return (self._pos, self._depth)