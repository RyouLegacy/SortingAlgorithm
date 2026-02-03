import time, testcase
import sort_algorithm.np as np
import sort_algorithm.heapsort as heapsort 
import sort_algorithm.quicksort as quicksort 
import sort_algorithm.mergesort as mergesort

dataset = testcase.test_case

dict = [
    ("Heap Sort", heapsort),
    ("Quick Sort", quicksort),
    ("Merge Sort", mergesort),
    ("Numpy Sort", np)
]

speed_time = []
for sort_type in range(4):
    object = dict[sort_type]
    print(f"Testing {object[0]} ....")

    counter = 0
    speed_ds = []
    for current_dataset in dataset:
        counter += 1
        current_tick = time.time()  
        object[1].run(current_dataset)
        
        runtime = int((time.time() - current_tick) * 1000)
        print(f"Dataset #{counter} took {runtime} ms!")

        speed_ds.append(runtime)
    
    speed_time.append(speed_ds)
    print(f"Average Timelimit: {sum(speed_ds) / 10}\n")

print(speed_time)