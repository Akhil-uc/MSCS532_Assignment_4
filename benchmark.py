# Import the random module to generate random test data.
import random

# Import the time module to measure algorithm execution time.
import time

# Import the heapq module for heap-related operations if needed.
import heapq

# Import the custom HeapSorter class.
from heapsort import HeapSorter


# Define a function that sorts a list using the Quick Sort algorithm.
def quick_sort(values):

    # Check whether the list contains one or zero elements.
    if len(values) <= 1:

        # Return the list because it is already sorted.
        return values

    # Select the middle element of the list as the pivot.
    pivot = values[len(values) // 2]

    # Create a list containing elements smaller than the pivot.
    lower = [x for x in values if x < pivot]

    # Create a list containing elements equal to the pivot.
    equal = [x for x in values if x == pivot]

    # Create a list containing elements greater than the pivot.
    higher = [x for x in values if x > pivot]

    # Recursively sort the lower and higher lists and combine all parts.
    return quick_sort(lower) + equal + quick_sort(higher)


# Define a function that sorts a list using the Merge Sort algorithm.
def merge_sort(values):

    # Check whether the list contains one or zero elements.
    if len(values) <= 1:

        # Return the list because it is already sorted.
        return values

    # Calculate the middle index of the list.
    middle = len(values) // 2

    # Recursively sort the left half of the list.
    left = merge_sort(values[:middle])

    # Recursively sort the right half of the list.
    right = merge_sort(values[middle:])

    # Create an empty list to store the merged result.
    result = []

    # Initialize an index for traversing the left list.
    i = 0

    # Initialize an index for traversing the right list.
    j = 0

    # Continue merging while both lists still contain elements.
    while i < len(left) and j < len(right):

        # Compare the current element from the left list with the current element from the right list.
        if left[i] < right[j]:

            # Add the smaller left element to the merged list.
            result.append(left[i])

            # Move to the next element in the left list.
            i += 1

        # Execute this block when the right element is smaller or equal.
        else:

            # Add the smaller right element to the merged list.
            result.append(right[j])

            # Move to the next element in the right list.
            j += 1

    # Add any remaining elements from the left list.
    result.extend(left[i:])

    # Add any remaining elements from the right list.
    result.extend(right[j:])

    # Return the completely sorted list.
    return result


# Create a list containing the input sizes for benchmarking.
sizes = [1000, 5000, 10000]

# Create an object of the HeapSorter class.
sorter = HeapSorter()

# Print a separator line.
print("-" * 60)

# Display the benchmark title.
print("Benchmark Results")

# Print another separator line.
print("-" * 60)

# Loop through each input size.
for amount in sizes:

    # Generate a list of unique random numbers.
    numbers = random.sample(range(amount * 10), amount)

    # Create a copy of the random numbers for HeapSort.
    copy1 = numbers.copy()

    # Create a copy of the random numbers for QuickSort.
    copy2 = numbers.copy()

    # Create a copy of the random numbers for MergeSort.
    copy3 = numbers.copy()

    # Record the starting time before HeapSort begins.
    start = time.perf_counter()

    # Sort the first copy using HeapSort.
    sorter.sort_numbers(copy1)

    # Calculate the total HeapSort execution time.
    heap_time = time.perf_counter() - start

    # Record the starting time before QuickSort begins.
    start = time.perf_counter()

    # Sort the second copy using QuickSort.
    quick_sort(copy2)

    # Calculate the total QuickSort execution time.
    quick_time = time.perf_counter() - start

    # Record the starting time before MergeSort begins.
    start = time.perf_counter()

    # Sort the third copy using MergeSort.
    merge_sort(copy3)

    # Calculate the total MergeSort execution time.
    merge_time = time.perf_counter() - start

    # Display the current input size.
    print(f"\nInput Size : {amount}")

    # Display the HeapSort execution time.
    print(f"HeapSort : {heap_time:.6f} sec")

    # Display the QuickSort execution time.
    print(f"QuickSort : {quick_time:.6f} sec")

    # Display the MergeSort execution time.
    print(f"MergeSort : {merge_time:.6f} sec")
