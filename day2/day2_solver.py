from typing import List
from day2.submarine import Submarine

def simulate_movement(cmds: List[str]):
    submarine = Submarine(0, 0)

    for cmd in cmds:
        submarine.move(cmd)

    pos, depth = submarine.get_location()
    
    return pos * depth