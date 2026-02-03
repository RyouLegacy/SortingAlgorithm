from typing import *

def run(array: List) -> List:

    def heapify(array: List, n: int, i: int):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and array[left_child] > array[largest]:
            largest = left_child
        if right_child < n and array[right_child] > array[largest]:
            largest = right_child

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, n, largest)

        return

    def heap_sort(array: List):
        length = len(array)

        for i in range(length // 2 - 1, -1, -1):
            heapify(array, length, i)

        for i in range(length - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, i, 0)

    heap_sort(array)

    return array

