### STACK IMPLEMENTATION LINKED LIST

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    #Work in LIFO order
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self,item):
        #Add elemnt in the stack
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        #Remove elemnt from the stack if present
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        #Display/return top element from the stack if present
        if self.is_empty():
            raise IndexError("Peek from Empty Stack")
        return self.top.data

    def is_empty(self):
        #Check if the stack is empty or not
        return self.top == None

    def size(self):
        #Return the length of the stack
        return self._size


if __name__ == "__main__":
    s = Stack()
    print("Is empty?", s.is_empty())

    s.push(5)
    s.push(15)
    s.push(25)

    print("Stack size:", s.size())
    print("Top element:", s.peek())

    print("Popped:", s.pop())
    print("After pop, top element:", s.peek())
    print("Stack size:", s.size())
