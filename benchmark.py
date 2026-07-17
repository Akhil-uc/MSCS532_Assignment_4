# Import modules used for benchmarking
import random
import time
import heapq

# Import the custom HeapSort implementation
from heapsort import HeapSorter

# Recursive Quick Sort implementation
def quick_sort(values):

    # Base case
    if len(values) <= 1:
        return values

    # Select the middle element as pivot
    pivot = values[len(values) // 2]

    # Divide elements into three groups
    lower = [x for x in values if x < pivot]
    equal = [x for x in values if x == pivot]
    higher = [x for x in values if x > pivot]

    return quick_sort(lower) + equal + quick_sort(higher)


# Recursive Merge Sort implementation
def merge_sort(values):

    # Base case
    if len(values) <= 1:
        return values

    # Split the list into two halves
    middle = len(values) // 2

    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    result = []

    i = 0
    j = 0

    # Merge the sorted halves
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input sizes used for benchmarking
sizes = [1000, 5000, 10000]

# Create a HeapSorter object
sorter = HeapSorter()

print("-" * 60)
print("Benchmark Results")
print("-" * 60)

# Run the benchmark for each input size
for amount in sizes:

    # Generate unique random numbers
    numbers = random.sample(range(amount * 10), amount)

    copy1 = numbers.copy()
    copy2 = numbers.copy()
    copy3 = numbers.copy()

    # Measure HeapSort execution time
    start = time.perf_counter()
    sorter.sort_numbers(copy1)
    heap_time = time.perf_counter() - start

    # Measure QuickSort execution time
    start = time.perf_counter()
    quick_sort(copy2)
    quick_time = time.perf_counter() - start

    # Measure MergeSort execution time
    start = time.perf_counter()
    merge_sort(copy3)
    merge_time = time.perf_counter() - start

    # Display benchmark results
    print(f"\nInput Size : {amount}")
    print(f"HeapSort : {heap_time:.6f} sec")
    print(f"QuickSort : {quick_time:.6f} sec")
    print(f"MergeSort : {merge_time:.6f} sec")
