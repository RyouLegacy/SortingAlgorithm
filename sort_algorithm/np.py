import numpy as np
from typing import *

def run(array: List) -> List:
    arr = np.array(array)
    return np.sort(arr).tolist()
