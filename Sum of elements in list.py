#approach1
#Input : [5,10,15,20]
#Output: 50

mylist=[5,10,15,20]
total=0

for i in range(0,len(mylist)):
    total=total+mylist[i]  #Index number

print("Sum of all elements in given list:", total)

#Approach2
mylist=[5,10,15,20]
total=sum(mylist)
print("Sum of all elements in given list:", total)





