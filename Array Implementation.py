### BASIC ARRAY IMPLEMENTATION IN PYTHON
import array as arr

# TO CREATE AN ARRAY USING ARRAY MODULE
arr1 = arr.array('i',[1,2,3,4,5])

# TO PRINT ARRAY MODULE
print(arr1)
# TO PRINT THE ARRAY ELEMENTS
print(*arr1)

# PACKING AND UNPACKING OF ARRAY 
a,b,c,d,e = arr1
print(a,b,c,d,e,sep=' ')

a, *b, c = arr1
print(a,b,c,sep=' ')

arr2 = arr.array('i',[1,3])
arr3 = arr.array('i',[2,5])
arr4 = [arr2,arr3]

(a,b),(c,d) = arr4
print(a,b)
print(c,d)

f, *r = arr[:2],arr[2:]
print(f)
print(r)
