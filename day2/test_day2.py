from day2.day2_input_loader import get_puzzle_input, get_small_input
from day2.day2_solver import simulate_movement

### Part 1

def test_smallInput_simulateMovement_150():
    expected = 150
    acctual = simulate_movement(get_small_input())
    assert acctual == expected

def test_puzzleInput_simulateMovement_1924923():
    expected = 1924923
    acctual = simulate_movement(get_puzzle_input())
    assert acctual == expected