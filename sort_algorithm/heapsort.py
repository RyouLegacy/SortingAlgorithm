from typing import *

def run(array: List) -> List:

    # Hàm heapify: đảm bảo cây con tại chỉ số i thỏa mãn tính chất max-heap
    def heapify(array: List, n: int, i: int):
        largest = i                 # Giả sử node hiện tại là lớn nhất
        left_child = 2 * i + 1      # Chỉ số con trái
        right_child = 2 * i + 2     # Chỉ số con phải

        # Nếu con trái tồn tại và lớn hơn node hiện tại
        if left_child < n and array[left_child] > array[largest]:
            largest = left_child

        # Nếu con phải tồn tại và lớn hơn node lớn nhất hiện tại
        if right_child < n and array[right_child] > array[largest]:
            largest = right_child

        # Nếu node lớn nhất không phải là node ban đầu
        if largest != i:
            # Hoán đổi giá trị
            array[i], array[largest] = array[largest], array[i]
            # Đệ quy heapify cho cây con bị ảnh hưởng
            heapify(array, n, largest)

        return

    # Hàm heap sort chính
    def heap_sort(array: List):
        length = len(array)

        # Xây dựng max-heap từ mảng ban đầu
        for i in range(length // 2 - 1, -1, -1):
            heapify(array, length, i)

        # Lần lượt đưa phần tử lớn nhất về cuối mảng
        for i in range(length - 1, 0, -1):
            array[i], array[0] = array[0], array[i]  # Đưa max về cuối
            heapify(array, i, 0)                     # Heapify phần còn lại

    # Thực hiện heap sort
    heap_sort(array)

    # Trả về mảng đã được sắp xếp
    return array