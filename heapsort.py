# Import the random module to generate random numbers for testing.
import random


# Define a class that performs HeapSort using a max heap.
class HeapSorter:

    # Define the constructor for the HeapSorter class.
    def __init__(self):

        # No initialization is required for this class.
        pass

    # Define a function that restores the max heap property.
    def heapify(self, values, heap_size, root):

        # Assume the root node is currently the largest value.
        largest_node = root

        # Calculate the index of the left child.
        left_child = (2 * root) + 1

        # Calculate the index of the right child.
        right_child = (2 * root) + 2

        # Check whether the left child exists and is larger than the current largest node.
        if left_child < heap_size and values[left_child] > values[largest_node]:

            # Update the largest node to the left child.
            largest_node = left_child

        # Check whether the right child exists and is larger than the current largest node.
        if right_child < heap_size and values[right_child] > values[largest_node]:

            # Update the largest node to the right child.
            largest_node = right_child

        # Check whether a larger child was found.
        if largest_node != root:

            # Swap the root node with the largest child.
            values[root], values[largest_node] = values[largest_node], values[root]

            # Recursively restore the heap property for the affected subtree.
            self.heapify(values, heap_size, largest_node)

    # Define a function that sorts a list using the HeapSort algorithm.
    def sort_numbers(self, values):

        # Store the total number of elements in the list.
        total_items = len(values)

        # Build a max heap by heapifying all non-leaf nodes.
        for current in range(total_items // 2 - 1, -1, -1):

            # Restore the heap property starting from the current node.
            self.heapify(values, total_items, current)

        # Repeatedly move the largest element to the end of the list.
        for last in range(total_items - 1, 0, -1):

            # Swap the root element with the last unsorted element.
            values[0], values[last] = values[last], values[0]

            # Restore the heap property for the remaining unsorted elements.
            self.heapify(values, last, 0)

        # Return the sorted list.
        return values


# Check whether this file is being run directly.
if __name__ == "__main__":

    # Generate a list of fifteen random numbers.
    numbers = [random.randint(10, 200) for _ in range(15)]

    # Display a heading before printing the unsorted list.
    print("Before Sorting")

    # Print the original list of numbers.
    print(numbers)

    # Create an object of the HeapSorter class.
    sorter = HeapSorter()

    # Sort the list using the HeapSort algorithm.
    sorter.sort_numbers(numbers)

    # Display a heading before printing the sorted list.
    print("\nAfter HeapSort")

    # Print the sorted list.
    print(numbers)
