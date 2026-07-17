import random

# HeapSort implementation using a max heap
class HeapSorter:

    def __init__(self):
        pass

    # Restore the heap property from the given root
    def heapify(self, values, heap_size, root):

        largest_node = root
        left_child = (2 * root) + 1
        right_child = (2 * root) + 2

        # Check if the left child is larger
        if left_child < heap_size and values[left_child] > values[largest_node]:
            largest_node = left_child

        # Check if the right child is larger
        if right_child < heap_size and values[right_child] > values[largest_node]:
            largest_node = right_child

        # Swap and continue heapifying if needed
        if largest_node != root:
            values[root], values[largest_node] = values[largest_node], values[root]
            self.heapify(values, heap_size, largest_node)

    # Perform HeapSort on the input list
    def sort_numbers(self, values):

        total_items = len(values)

        # Build a max heap
        for current in range(total_items // 2 - 1, -1, -1):
            self.heapify(values, total_items, current)

        # Extract elements one by one
        for last in range(total_items - 1, 0, -1):
            values[0], values[last] = values[last], values[0]
            self.heapify(values, last, 0)

        return values


# Example usage
if __name__ == "__main__":

    numbers = [random.randint(10, 200) for _ in range(15)]

    print("Before Sorting")
    print(numbers)

    sorter = HeapSorter()

    sorter.sort_numbers(numbers)

    print("\nAfter HeapSort")
    print(numbers)
