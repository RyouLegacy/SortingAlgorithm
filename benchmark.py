import time, testcase
import sort_algorithm.np as np
import sort_algorithm.heapsort as heapsort 
import sort_algorithm.quicksort as quicksort 
import sort_algorithm.mergesort as mergesort

# Tập dữ liệu test
dataset = testcase.test_case

# Danh sách các thuật toán sắp xếp cần benchmark
dict = [
    ("Heap Sort", heapsort),
    ("Quick Sort", quicksort),
    ("Merge Sort", mergesort),
    ("Numpy Sort", np)
]

speed_time = []  # Lưu thời gian chạy của từng thuật toán

# Lặp qua từng thuật toán
for sort_type in range(4):
    object = dict[sort_type]
    print(f"Testing {object[0]} ....")

    counter = 0
    speed_ds = []  # Lưu thời gian của từng dataset

    # Chạy thuật toán trên từng bộ dữ liệu
    for current_dataset in dataset:
        counter += 1

        # Bắt đầu đo thời gian
        current_tick = time.time()
        object[1].run(current_dataset)

        # Tính thời gian chạy (ms)
        runtime = int((time.time() - current_tick) * 1000)
        print(f"Dataset #{counter} took {runtime} ms!")

        speed_ds.append(runtime)
    
    # Lưu kết quả của thuật toán hiện tại
    speed_time.append(speed_ds)

    # In thời gian chạy trung bình
    print(f"Average Timelimit: {sum(speed_ds) / 10}\n")

# In toàn bộ kết quả benchmark
print(speed_time)
