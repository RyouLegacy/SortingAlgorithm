from typing import List
from random import *
import numpy as np

# Giới hạn các số
MIN = 1
MAX = 10**9

# Sinh một dãy ngẫu nhiên tăng dần
def generate_increased_array(length: int) -> List:
    # Số đầu tiên
    temp = uniform(MIN, MAX)
    
    # Khởi tạo mảng kết quả
    array = np.empty(length, dtype=float)
    array[0] = temp
    for step in range(length - 1):
        # Vì mảng tăng dần chúng ta chỉ random trong khoảng (temp, MAX)
        # Và sau đó cập nhật lại temp
        array[step + 1] = uniform(temp, MAX)
        temp = array[step + 1]

    return array


# Sinh một dãy ngẫu nhiên giảm dần
def generate_decreased_array(length: int) -> List:
    # Số đầu tiên
    temp = uniform(MIN, MAX)

    # Khởi tạo mảng kết quả
    array = np.empty(length, dtype=float)
    array[0] = temp
    for step in range(length - 1):
        # Vì mảng giảm dần chúng ta chỉ random trong khoảng (MIN, temp)
        # Và sau đó cập nhật lại temp
        array[step + 1] = uniform(MIN, temp)
        temp = array[step + 1]

    return array

# Sinh ra một dãy ngẫu nhiên
# Nếu isFloat == True thì dãy là số thực còn không thì là số nguyên 
def generate_random_array(length: int, isFloat: bool) -> List:
    # Khởi tạo mảng 
    if isFloat:
        array = np.random.uniform(MIN, MAX, length)
    else:
        array = np.random.randint(MIN, MAX + 1, length)

    return array

LENGTH = int(1e6)

test_case = np.array([
    generate_increased_array(LENGTH),
    generate_decreased_array(LENGTH),
    *[generate_random_array(LENGTH, True) for _ in range(4)],
    *[generate_random_array(LENGTH, False) for _ in range(4)]
], dtype=object)