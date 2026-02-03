import numpy as np
from typing import *

def run(array: List) -> List:
    # Chuyển list Python sang mảng NumPy
    arr = np.array(array)

    # Sử dụng hàm sort của NumPy để sắp xếp mảng
    return np.sort(arr).tolist()  # Chuyển lại về list Python
