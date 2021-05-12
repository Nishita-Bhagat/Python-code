# Input : mylist = [1,2,3,4,1,5,6,2,2,5,2,2]

# Method 1 : Using loop
mylist = [1,2,3,4,1,5,6,2,2,5,2,2]
x = 2
count = 0
for element in mylist:
    if (element==x):
        count=count+1
print("{} has occured {} times".format(x,count))


# Method 2 : Using count()
mylist = [1,2,3,4,1,5,6,2,2,5,2,2]
x = 5
print("{} has occured {} times".format(x,mylist.count(x)))


# Method 3 : Using Counter()
from collections import Counter
mylist = [1,2,3,4,1,5,6,2,2,5,2,2]
x = 2
dict = Counter(mylist)
print("{} has occured {} times".format(x,dict[x]))
