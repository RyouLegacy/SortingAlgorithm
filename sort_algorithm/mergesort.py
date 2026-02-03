from typing import *

def run(array: List) -> List:

    # Thuật toán Merge Sort (sắp xếp trộn)
    def merge_sort(array: List):
        # Điều kiện dừng: mảng chỉ còn 1 phần tử
        if len(array) == 1:
            return

        # Chia mảng thành hai nửa
        mid = len(array) >> 1
        left_array = array[:mid]
        right_array = array[mid:]

        # Đệ quy sắp xếp hai nửa
        merge_sort(left_array)
        merge_sort(right_array)

        pos_left = 0     # Con trỏ mảng trái
        pos_right = 0    # Con trỏ mảng phải
        counter = 0      # Vị trí ghi vào mảng gốc

        # Trộn hai mảng con đã được sắp xếp
        while pos_left < len(left_array) and pos_right < len(right_array):
            if left_array[pos_left] <= right_array[pos_right]:
                array[counter] = left_array[pos_left]
                pos_left += 1
            else:
                array[counter] = right_array[pos_right]
                pos_right += 1
            counter += 1

        # Sao chép các phần tử còn lại của mảng trái (nếu có)
        if pos_left < len(left_array):
            array[counter:] = left_array[pos_left:]

        # Sao chép các phần tử còn lại của mảng phải (nếu có)
        if pos_right < len(right_array):
            array[counter:] = right_array[pos_right:]

        return

    # Gọi merge sort cho toàn bộ mảng
    merge_sort(array)

    return
