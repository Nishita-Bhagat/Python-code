#mylist = [1,6,3,5,3,4]

#Approach 1: Using loop
mylist = [1,6,3,5,3,4]
element=8
flag=0
for i in mylist:
    if(i==element):
        print("Element found")
        flag=1
        break
if(flag==0):
    print("Element not found")

#Approach 2 : Using in operator
mylist = [1,6,3,5,3,4]
ele=5
if(ele in mylist):
    print("Element found")
else:
    print("Element not found")