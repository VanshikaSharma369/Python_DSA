### QUEUE IMPLEMENTATION USING LIST

class Queue:
    # Work in FIFO order
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        #Add Element in the queue
        self.queue.append(item)

    def dequeue(self):
        #Remove top element from the queue if present
        if self.is_empty():
            raise IndexError("Dequeue from empty queue.")
        return self.queue.pop(0)

    def peek(self):
        # Return/Display top element from the queue if present
        if self.is_empty():
            raise IndexError("Peek from Empty Queue")
        return self.queue[0]

    def is_empty(self):
        #Return if the queue is empty or not
        return len(self.queue)==0

    def size(self):
        #Return the size of the queue
        return len(self.queue)

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
