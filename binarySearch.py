#Binary Search
#Time complexity O(logn) 
import numpy as np
import timeit


def main():

    num_items = 100
    num_to_find = 100
    dataset = np.random.randint(1,200,num_items)

    for i in range(len(dataset)-1,0,-1):
        for j in range(i):
            if(dataset[j] > dataset[j+1]):
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp


    timer_start = timeit.default_timer()

    print(binary_search(num_items-1, 0, num_to_find, dataset))

    timer_end = timeit.default_timer()

    print(str(timer_end - timer_start) + " seconds to execute")

def binary_search(high, low, key, list):
    if(high < low):
        return "Number not found"
    else:
        center = round(high-low /2)
    if(key < list[center]):
        return binary_search(center-1, low, key, list)
    elif(key > list[center]):
        return binary_search(high, center+1, key, list)
    else:
        return "Number FOUND at " + str(center)


main()
