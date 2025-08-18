
### STACK IMPLEMENTATION USING LIST IN PYTHON

class Stack:
    # Work in LIFO Order
    def __init__(self):
        self.stack = []

    def push(self,item):
        # Add element in the stack
        self.stack.append(item)

    def pop(self):
        # remove top element from the stack if present
        if self.is_empty():
            raise IndexError("Pop from Empty Stack")
        return self.stack.pop()

    def peek(self):
        # return/display top element from the stack if present
        if self.is_empty():
            raise IndexError("Peek from Empty Stack")
        return self.stack[-1]

    def is_empty(self):
        #check if the stack is empty or not
        return len(self.stack)==0

    def size(self):
        #return/display the size of the stack
        return len(self.stack)


if __name__ == "__main__":

    s = Stack()
    print("Is empty?", s.is_empty())

    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack size:", s.size())
    print("Top element:", s.peek())

    print("Popped:", s.pop())
    print("After pop, top element:", s.peek())
    print("Stack size:", s.size())
