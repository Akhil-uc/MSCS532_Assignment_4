import random
import time
import heapq


from heapsort import HeapSorter


def quick_sort(values):

    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]

    lower = [x for x in values if x < pivot]

    equal = [x for x in values if x == pivot]

    higher = [x for x in values if x > pivot]

    return quick_sort(lower) + equal + quick_sort(higher)


def merge_sort(values):

    if len(values) <= 1:
        return values

    middle = len(values) // 2

    left = merge_sort(values[:middle])

    right = merge_sort(values[middle:])

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


sizes = [1000, 5000, 10000]

sorter = HeapSorter()

print("-" * 60)
print("Benchmark Results")
print("-" * 60)

for amount in sizes:

    numbers = random.sample(range(amount * 10), amount)

    copy1 = numbers.copy()
    copy2 = numbers.copy()
    copy3 = numbers.copy()

    start = time.perf_counter()

    sorter.sort_numbers(copy1)

    heap_time = time.perf_counter() - start

    start = time.perf_counter()

    quick_sort(copy2)

    quick_time = time.perf_counter() - start

    start = time.perf_counter()

    merge_sort(copy3)

    merge_time = time.perf_counter() - start

    print(f"\nInput Size : {amount}")

    print(f"HeapSort : {heap_time:.6f} sec")

    print(f"QuickSort : {quick_time:.6f} sec")

    print(f"MergeSort : {merge_time:.6f} sec")