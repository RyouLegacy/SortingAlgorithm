import random
from typing import *

def run(array: List) -> List:
    is_increasing = all(array[i] <= array[i+1] for i in range(len(array)-1))
    if is_increasing: return
    
    is_decreasing = all(array[i] >= array[i+1] for i in range(len(array)-1))
    if is_decreasing:
        array.reverse()
        return
    
    def divide(array: List, L: int, R: int) -> int:
        pivot_index = random.randint(L, R)
        array[pivot_index], array[R] = array[R], array[pivot_index]

        current = L - 1
        pivot = array[R]

        for i in range(L, R):
            if array[i] <= pivot:
                current += 1
                array[current], array[i] = array[i], array[current]

        current += 1
        array[R], array[current] = array[current], array[R]

        return current
    def quick_sort(array: List, L: int, R: int):
        if L >= R:
            return
        split = divide(array, L, R)
        quick_sort(array, L, split - 1)
        quick_sort(array, split + 1, R)

    quick_sort(array, 0, len(array) - 1)

    return
