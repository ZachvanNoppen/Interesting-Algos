#Selection Sort
import numpy as np
import timeit

num_items = 1000

dataset = np.random.randint(1,200,num_items)


print("Unsorted Array:\n\n ")
print(dataset)
print("\n\n")

timer_start = timeit.default_timer()

for i in range(len(dataset)):
    smallest_index = i
    for j in range(i+1,len(dataset)):
        if(dataset[j] < dataset[smallest_index]):
            smallest_index = j

    current_num = dataset[i]
    dataset[i] = dataset[smallest_index]
    dataset[smallest_index] = current_num

timer_end = timeit.default_timer()

print("Sorted Array:\n\n ")
print(dataset)
print("\n\n It completed with a runtime of " + str(timer_end - timer_start) + " seconds")
