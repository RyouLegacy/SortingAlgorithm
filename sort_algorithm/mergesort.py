from typing import *

def run(array: List) -> List:

    def merge_sort(array: List):
        if len(array) == 1: 
            return
        mid = len(array) >> 1
        left_array = array[:mid]
        right_array = array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        pos_left = 0
        pos_right = 0
        counter = 0
        while pos_left < len(left_array) and pos_right < len(right_array):
            if left_array[pos_left] <= right_array[pos_right]:
                array[counter] = left_array[pos_left]
                pos_left += 1
            else:
                array[counter] = right_array[pos_right]
                pos_right += 1
            counter += 1
        

        if pos_left < len(left_array):
            array[counter:] = left_array[pos_left:]

        if pos_right < len(right_array):
            array[counter:] = right_array[pos_right:]

        return
    
    merge_sort(array)

    return