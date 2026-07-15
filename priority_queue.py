class Task:

    def __init__(self, task_id, priority, arrival, deadline):

        self.task_id = task_id
        self.priority = priority
        self.arrival = arrival
        self.deadline = deadline

    def __str__(self):

        return f"{self.task_id}  Priority={self.priority}"


class PriorityQueue:

    def __init__(self):

        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return (2 * index) + 1

    def right(self, index):
        return (2 * index) + 2

    def is_empty(self):

        return len(self.heap) == 0

    def insert(self, task):

        self.heap.append(task)

        current = len(self.heap) - 1

        while current > 0 and self.heap[current].priority > self.heap[self.parent(current)].priority:

            p = self.parent(current)

            self.heap[current], self.heap[p] = self.heap[p], self.heap[current]

            current = p

    def heapify_down(self, index):

        size = len(self.heap)

        while True:

            left = self.left(index)
            right = self.right(index)

            biggest = index

            if left < size and self.heap[left].priority > self.heap[biggest].priority:
                biggest = left

            if right < size and self.heap[right].priority > self.heap[biggest].priority:
                biggest = right

            if biggest == index:
                break

            self.heap[index], self.heap[biggest] = self.heap[biggest], self.heap[index]

            index = biggest

    def extract_max(self):

        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        highest = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return highest

    def increase_priority(self, task_id, new_priority):

        for index in range(len(self.heap)):

            if self.heap[index].task_id == task_id:

                if new_priority < self.heap[index].priority:
                    return

                self.heap[index].priority = new_priority

                while index > 0 and self.heap[index].priority > self.heap[self.parent(index)].priority:

                    p = self.parent(index)

                    self.heap[index], self.heap[p] = self.heap[p], self.heap[index]

                    index = p

                break


if __name__ == "__main__":

    scheduler = PriorityQueue()

    scheduler.insert(Task("T1", 20, 1, 5))
    scheduler.insert(Task("T2", 90, 2, 8))
    scheduler.insert(Task("T3", 45, 3, 10))
    scheduler.insert(Task("T4", 60, 4, 12))

    print("Highest Priority Task")

    print(scheduler.extract_max())

    scheduler.increase_priority("T1", 95)

    print("\nAfter Increasing Priority")

    while not scheduler.is_empty():

        print(scheduler.extract_max())