import ctypes

"""         What is ctypes in Python?

ctypes is a built-in Python foreign function library.

It allows Python code to call C functions and use low-level memory management.

It’s often used when we want to allocate raw memory blocks, just like C arrays.


"""

class Dynamic_Array:
    def __init__(self):
        self.n = 0 #number of elements
        self.capacity = 1 #initial capacity
        self.A = self.make_Array(self.capacity)

    def __len__(self):
        return self.n

    """You noticed things like __len__(), __getitem__(), etc. Those are called dunder methods (short for “double underscore” methods) or magic methods in Python.

They allow us to customize how our objects behave with built-in Python functions and operators.

So __len__ makes your object compatible with the built-in len() function."""

    def __getitem__(self,index):
        if not 0 <= index < self.n:
            raise IndexError("Index out of bound error!")
        return self.A[index]

    def append(self,item):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = item
        self.n += 1

    def _resize(self,new_cap):
        B = self.make_Array(new_cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    def make_Array(self,capacity):
        return (capacity * ctypes.py_object)()
    """ (capacity * ctypes.py_object) creates a C array that can store Python objects.

() at the end actually allocates memory for that array.

This gives us a low-level array with a fixed capacity (like in C), instead of Python’s built-in list (which hides all that complexity).  """


if __name__ == "__main__":
    arr = Dynamic_Array()

    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.append(40)

    print("Array len", len(arr))
    print("Element at index 3:",arr[3])


