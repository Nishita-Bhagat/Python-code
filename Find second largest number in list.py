# Input : mylist = [70,30,20,100,40,80]

#Method 1 : Sorting
mylist = [70,30,20,100,40,80]
mylist.sort()
print(mylist)

print('Largest number is:',mylist[-1])
print('Second largest number is:', mylist[-2])

#m Method 2
mylist = [70,30,20,100,40,80]
new_list = set(mylist)
new_list.remove(max(new_list))  #100 is removed
print(new_list)
print(max(new_list))
