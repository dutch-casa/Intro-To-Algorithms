'''
COMP 3270 Intro to Algorithms Homework 1: Introduction to Python
install python (google it) and make sure you have python version 3.6+ 
'''
import random
import time
import matplotlib.pyplot as plt

'''
Problem 1: Implement merge sort
'''
# your code here
def merge(l, r):
    #results array to return
    merged = []
    i = j = 0
    
    #while pointers are in bounds
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            #if left element is less than right element
            #add left element to results
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
    
    #add remaining elements
    merged.extend(l[i:])
    merged.extend(r[j:])
    return merged       

def merge_sort(arr):
    #base case
    if len(arr) <= 1:
        return arr
    #find mid, sort left and right
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


'''
Problem 2: Implement quick sort 2 ways. 1 using a random element as the pivot. 2nd
using the median of 3 random elements as the pivot
'''
#your code here

# i hope you don't mind im adding the swap helper
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high, pivot_index):
    swap(arr, pivot_index, high)
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def quick_sort_rand(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        pivot_index = partition(arr, low, high, pivot_index)
        quick_sort_rand(arr, low, pivot_index - 1)
        quick_sort_rand(arr, pivot_index + 1, high)

def median_of_three(arr, low, high):
    r1 = random.randint(low, high)
    r2 = random.randint(low, high)
    r3 = random.randint(low, high)
    a, b, c = arr[r1], arr[r2], arr[r3]
    if a <= b <= c or c <= b <= a:
        return r2
    elif b <= a <= c or c <= a <= b:
        return r1
    else:
        return r3


def quick_sort_median(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high, median_of_three(arr, low, high))
        quick_sort_median(arr, low, pivot_index - 1)
        quick_sort_median(arr, pivot_index + 1, high)


def median_lmh(arr, low, high):
    mid = (low + high) // 2

    a, b, c = arr[low], arr[mid], arr[high]

    if (a <= b <= c) or (c <= b <= a):
        return mid
    elif (b <= a <= c) or (c <= a <= b):
        return low
    else:
        return high

#real talk not happy with the overhead picking three random ones introduces so im going to do another one without
# using random because median of three SHOULD be faster!!!
def quick_sort_median2(arr, low, high):
    if low < high:
        pivot_index = median_lmh(arr, low, high)
        pivot_index = partition(arr, low, high, pivot_index)
        quick_sort_median2(arr, low, pivot_index - 1)
        quick_sort_median2(arr, pivot_index + 1, high)



'''
Problem 3: Compare the runtime between merge sort, quick sort with random pivot,
and quick sort with median of 3 random elements on lists ranging from 100k to 2m by
increments of 100k
use the time package to get the time, so use start = time.time() then after the
algorithm runs end = time.time()
make a graph of this. I recommend the ggplot python port plotnine, but matplotlib
would be fine as well
'''
#your code here
# inputs might look like A = [random.randint(0,1000000000) for i in range(100000)]

def benchmark_sorting_algorithms():
    #sizes step variable
    sizes = range(100000, 2000001, 100000)

    #arrays to store different time outputs
    merge_times = []
    quick_rand_times = []
    quick_median_times = []
    median_lmh_times = []
    
    #loop through sizes
    for size in sizes:
        #make an array of random numbers of size
        A = [random.randint(0, 1000000000) for _ in range(size)]
        print(f"Testing list of size {size}")
        #create copys for each algo
        A1 = [x for x in A]
        A2 = [x for x in A]
        A3 = [x for x in A]
        A4 = [x for x in A]

        # Benchmark merge sort
        start = time.time()
        merge_sort(A1)
        end = time.time()
        #push time on array for results
        merge_times.append(end - start)

        # Benchmark quick sort with random pivot
        start = time.time()
        quick_sort_rand(A2, 0, len(A2) - 1)
        end = time.time()
        #push time on array for results
        quick_rand_times.append(end - start)

        # Benchmark quick sort with median of three random elements
        start = time.time()
        quick_sort_median(A3, 0, len(A3) - 1)
        end = time.time()
        #push time on array for results
        quick_median_times.append(end - start)

        # benchmark quicksort with median of three deterministic elements
        start = time.time()
        quick_sort_median2(A4, 0, len(A4) - 1)
        end = time.time()
        #push time on array for results
        median_lmh_times.append(end - start)

    return sizes, merge_times, quick_rand_times, quick_median_times, median_lmh_times


# Run the benchmark and assign to vars for plotting
sizes, merge_times, quick_rand_times, quick_median_times, median_lmh_times= benchmark_sorting_algorithms()

plt.figure(figsize=(10, 6))
plt.plot(sizes, merge_times, 'o-', label='Merge Sort')
plt.plot(sizes, quick_rand_times, 'o-', label='Quick Sort (Random Pivot)')
plt.plot(sizes, quick_median_times, 'o-', label='Quick Sort (Median of Three)')
plt.plot(sizes, median_lmh_times, 'o-', label='Quick Sort (Median of Three (no randomness))')

plt.xlabel('List Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Runtime Comparison')
plt.legend()
plt.grid(True)
plt.show()

