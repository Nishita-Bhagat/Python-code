# Input : list1 = [3,2,4]
# Output : 24
# Explanation : 3*2*4=24

#Method 1 : Traversal
mylist = [3,2,4]
result = 1

for x in mylist:
    result = result * x
print(result)

#Method 2 : Using Numpy package.
import numpy
mylist = [3,2,4]
result = numpy.prod(mylist)
print(result)