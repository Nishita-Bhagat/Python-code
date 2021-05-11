#mylist = [20,30,40,50,1,100,90]

#Approach1 : Sort the list in ascending order and print the first and last element in the list.
mylist = [20,30,40,50,1,100,90]
mylist.sort()  #Sorting
print(mylist)  #[1, 20, 30, 40, 50, 90, 100]

print("Smallest element is:",mylist[0])
print("Largest element is:",mylist[-1])

#Approach2 : Using min() and max() methods
mylist = [20,30,40,50,1,100,90]
print("Smallest is:",min(mylist))
print("Largest is:",max(mylist))


