import random


class HeapSorter:

    def __init__(self):
        pass

    def heapify(self, values, heap_size, root):

        largest_node = root
        left_child = (2 * root) + 1
        right_child = (2 * root) + 2

        if left_child < heap_size and values[left_child] > values[largest_node]:
            largest_node = left_child

        if right_child < heap_size and values[right_child] > values[largest_node]:
            largest_node = right_child

        if largest_node != root:
            values[root], values[largest_node] = values[largest_node], values[root]
            self.heapify(values, heap_size, largest_node)

    def sort_numbers(self, values):

        total_items = len(values)

        for current in range(total_items // 2 - 1, -1, -1):
            self.heapify(values, total_items, current)

        for last in range(total_items - 1, 0, -1):
            values[0], values[last] = values[last], values[0]
            self.heapify(values, last, 0)

        return values


if __name__ == "__main__":

    numbers = [random.randint(10, 200) for _ in range(15)]

    print("Before Sorting")
    print(numbers)

    sorter = HeapSorter()

    sorter.sort_numbers(numbers)

    print("\nAfter HeapSort")
    print(numbers)