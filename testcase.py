from typing import List
from random import *

# Giới hạn các số
MIN = 1
MAX = 10**9

# Sinh một dãy ngẫu nhiên tăng dần
def generate_increased_array(length: int) -> List:
    # Số đầu tiên
    temp = uniform(MIN, MAX)
    
    # Khởi tạo mảng kết quả
    array = [temp]
    for step in range(length - 1):
        # Vì mảng tăng dần chúng ta chỉ random trong khoảng (temp, MAX)
        # Và sau đó cập nhật lại temp
        array.append(
            uniform(temp, MAX)
        )
        temp = array[step + 1]

    return array


# Sinh một dãy ngẫu nhiên giảm dần
def generate_decreased_array(length: int) -> List:
    # Số đầu tiên
    temp = uniform(MIN, MAX)

    # Khởi tạo mảng kết quả
    array = [temp]
    for step in range(length - 1):
        # Vì mảng giảm dần chúng ta chỉ random trong khoảng (MIN, temp)
        # Và sau đó cập nhật lại temp
        array.append(
            uniform(MIN, temp)
        )
        temp = array[step + 1]

    return array

# Sinh ra một dãy ngẫu nhiên
# Nếu isFloat == True thì dãy là số thực còn không thì là số nguyên 
def generate_random_array(length: int, isFloat: bool) -> List:
    # Khởi tạo mảng 
    array = []

    for step in range(length):
        if isFloat:
            array.append(uniform(MIN, MAX))
        else:
            array.append(randint(MIN, MAX))

    return array

test_case = []

LENGTH = int(1e6)
test_case.append(generate_increased_array(LENGTH))
test_case.append(generate_decreased_array(LENGTH))
for float in range(4):
    test_case.append(generate_random_array(LENGTH, True))
for integer in range(4):
    test_case.append(generate_random_array(LENGTH, False))