# Define a class that represents a task with scheduling information.
class Task:

    # Define the constructor that creates a new task.
    def __init__(self, task_id, priority, arrival, deadline):

        # Store the unique identifier for the task.
        self.task_id = task_id

        # Store the priority assigned to the task.
        self.priority = priority

        # Store the task's arrival time.
        self.arrival = arrival

        # Store the task's deadline.
        self.deadline = deadline

    # Define a function that returns a readable string representation of the task.
    def __str__(self):

        # Return the task ID and its priority as a formatted string.
        return f"{self.task_id}  Priority={self.priority}"


# Define a priority queue class that uses a binary max heap.
class PriorityQueue:

    # Define the constructor that creates an empty priority queue.
    def __init__(self):

        # Create an empty list that will store the heap elements.
        self.heap = []

    # Define a function that returns the parent index of a node.
    def parent(self, index):

        # Calculate and return the parent index.
        return (index - 1) // 2

    # Define a function that returns the left child index of a node.
    def left(self, index):

        # Calculate and return the left child index.
        return (2 * index) + 1

    # Define a function that returns the right child index of a node.
    def right(self, index):

        # Calculate and return the right child index.
        return (2 * index) + 2

    # Define a function that checks whether the priority queue is empty.
    def is_empty(self):

        # Return True if the heap contains no elements.
        return len(self.heap) == 0

    # Define a function that inserts a new task into the priority queue.
    def insert(self, task):

        # Add the new task to the end of the heap.
        self.heap.append(task)

        # Store the index of the newly inserted task.
        current = len(self.heap) - 1

        # Continue moving the task upward while it has a higher priority than its parent.
        while current > 0 and self.heap[current].priority > self.heap[self.parent(current)].priority:

            # Calculate the parent's index.
            p = self.parent(current)

            # Swap the task with its parent.
            self.heap[current], self.heap[p] = self.heap[p], self.heap[current]

            # Move to the parent's position and continue checking.
            current = p

    # Define a function that restores the heap property after removing the root.
    def heapify_down(self, index):

        # Store the current number of elements in the heap.
        size = len(self.heap)

        # Continue checking until the heap property is restored.
        while True:

            # Calculate the index of the left child.
            left = self.left(index)

            # Calculate the index of the right child.
            right = self.right(index)

            # Assume the current node is the largest.
            biggest = index

            # Check whether the left child has a higher priority.
            if left < size and self.heap[left].priority > self.heap[biggest].priority:

                # Update the largest node to the left child.
                biggest = left

            # Check whether the right child has a higher priority.
            if right < size and self.heap[right].priority > self.heap[biggest].priority:

                # Update the largest node to the right child.
                biggest = right

            # Check whether the current node is already the largest.
            if biggest == index:

                # Stop because the heap property has been restored.
                break

            # Swap the current node with the largest child.
            self.heap[index], self.heap[biggest] = self.heap[biggest], self.heap[index]

            # Continue heapifying from the new position.
            index = biggest

    # Define a function that removes and returns the highest-priority task.
    def extract_max(self):

        # Check whether the priority queue is empty.
        if self.is_empty():

            # Return None because there are no tasks to remove.
            return None

        # Check whether only one task exists in the heap.
        if len(self.heap) == 1:

            # Remove and return the only task.
            return self.heap.pop()

        # Store the highest-priority task located at the root.
        highest = self.heap[0]

        # Move the last task in the heap to the root position.
        self.heap[0] = self.heap.pop()

        # Restore the heap property after replacing the root.
        self.heapify_down(0)

        # Return the removed highest-priority task.
        return highest

    # Define a function that increases the priority of an existing task.
    def increase_priority(self, task_id, new_priority):

        # Loop through every task stored in the heap.
        for index in range(len(self.heap)):

            # Check whether the current task matches the requested task ID.
            if self.heap[index].task_id == task_id:

                # Check whether the new priority is actually higher.
                if new_priority < self.heap[index].priority:

                    # Exit the function because the priority should not decrease.
                    return

                # Update the task with the new priority value.
                self.heap[index].priority = new_priority

                # Continue moving the task upward while its priority is greater than its parent's priority.
                while index > 0 and self.heap[index].priority > self.heap[self.parent(index)].priority:

                    # Calculate the parent's index.
                    p = self.parent(index)

                    # Swap the task with its parent.
                    self.heap[index], self.heap[p] = self.heap[p], self.heap[index]

                    # Continue checking from the parent's position.
                    index = p

                # Exit the loop because the task has been updated.
                break


# Check whether this file is being run directly.
if __name__ == "__main__":

    # Create a new priority queue that will act as the scheduler.
    scheduler = PriorityQueue()

    # Insert the first task into the scheduler.
    scheduler.insert(Task("T1", 20, 1, 5))

    # Insert the second task into the scheduler.
    scheduler.insert(Task("T2", 90, 2, 8))

    # Insert the third task into the scheduler.
    scheduler.insert(Task("T3", 45, 3, 10))

    # Insert the fourth task into the scheduler.
    scheduler.insert(Task("T4", 60, 4, 12))

    # Display a heading before extracting the highest-priority task.
    print("Highest Priority Task")

    # Remove and display the task with the highest priority.
    print(scheduler.extract_max())

    # Increase the priority of task T1.
    scheduler.increase_priority("T1", 95)

    # Display a heading after updating the task priority.
    print("\nAfter Increasing Priority")

    # Continue processing tasks until the priority queue becomes empty.
    while not scheduler.is_empty():

        # Remove and display the next highest-priority task.
        print(scheduler.extract_max())
