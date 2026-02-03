import random
from typing import *

def run(array: List) -> List:
    # Kiểm tra mảng đã được sắp xếp tăng dần hay chưa
    is_increasing = all(array[i] <= array[i + 1] for i in range(len(array) - 1))
    if is_increasing:
        return

    # Kiểm tra mảng đã được sắp xếp giảm dần hay chưa
    is_decreasing = all(array[i] >= array[i + 1] for i in range(len(array) - 1))
    if is_decreasing:
        # Đảo ngược mảng để được thứ tự tăng dần
        array.reverse()
        return

    # Hàm chia mảng (partition) dùng pivot ngẫu nhiên
    def divide(array: List, L: int, R: int) -> int:
        # Chọn pivot ngẫu nhiên và đưa về cuối đoạn
        pivot_index = random.randint(L, R)
        array[pivot_index], array[R] = array[R], array[pivot_index]

        current = L - 1      # Ranh giới các phần tử <= pivot
        pivot = array[R]     # Giá trị pivot

        # Duyệt và phân chia các phần tử theo pivot
        for i in range(L, R):
            if array[i] <= pivot:
                current += 1
                array[current], array[i] = array[i], array[current]

        # Đưa pivot về đúng vị trí cuối cùng
        current += 1
        array[R], array[current] = array[current], array[R]

        return current

    # Thuật toán Quick Sort đệ quy
    def quick_sort(array: List, L: int, R: int):
        # Điều kiện dừng đệ quy
        if L >= R:
            return

        # Chia mảng và sắp xếp hai nửa
        split = divide(array, L, R)
        quick_sort(array, L, split - 1)
        quick_sort(array, split + 1, R)

    # Bắt đầu sắp xếp toàn bộ mảng
    quick_sort(array, 0, len(array) - 1)

    return
