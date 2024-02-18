from typing import List


def get_most_common_bit(numbers: List[int], mask: int) -> int:
    masked = [number & mask for number in numbers]
    ones = sum([1 for number in masked if number > 0])
    return 1 if ones >= len(numbers) / 2 else 0

def get_masks(length: int):
    return [2**x for x in reversed(range(length))]

def analyze_data(numbers: List[int], length: int):
    masks = get_masks(length)
    most_common_bits = [get_most_common_bit(numbers, mask) for mask in masks]
    epsilon = int(''.join([str(bit) for bit in most_common_bits]), 2)
    gamma = (~epsilon) & ((2**length)-1)
    return (epsilon, gamma)