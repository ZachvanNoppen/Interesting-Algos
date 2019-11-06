#Selection Sort
import numpy as np
import timeit

num_items = 100

dataset = np.random.randint(1,200,num_items)

print("Unsorted Array:\n\n ")
print(dataset)
print("\n\n")

timer_start = timeit.default_timer()

for i in range(len(dataset)-1,0,-1):
    for j in range(i):
        if(dataset[j] > dataset[j+1]):
            temp = dataset[j]
            dataset[j] = dataset[j+1]
            dataset[j+1] = temp


timer_end = timeit.default_timer()

print("Sorted Array:\n\n ")
print(dataset)
print("\n\n It completed with a runtime of " + str(timer_end - timer_start) + " seconds")
