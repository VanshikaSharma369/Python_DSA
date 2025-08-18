### Queue Implementation using Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    # works in FIFO  Order
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self,item):
        #Add element in the queue
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        #Remove top element from the queue if present
        if self.is_empty():
            raise IndexError("Removing from Empty Queue")
        data = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        self._size -= 1
        return data

    def peek(self):
        # Return/Display element from the queue if present
        if self.is_empty():
            raise IndexError("Peek from the Empty Queue")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size


if __name__ == "__main__":

    q = Queue()
    print("Is empty?", q.is_empty())

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue size:", q.size())
    print("Front element:", q.peek())

    print("Dequeued:", q.dequeue())
    print("After dequeue, front element:", q.peek())
    print("Queue size:", q.size())
