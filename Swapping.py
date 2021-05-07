#num1=10
#num2=20

num1=input("Enter num1 value:")
num2=input("Enter num2 value:")

print("Value of num1 before swapping :", num1)
print("Value of num2 before swapping :", num2)

#Approach1
#temp=num1   #10 is stored in temp
#num1=num2   #20 is stored in num1
#num2=temp   #10 is stored in num2

#Approach2
num1,num2=num2,num1


print("Value of num1 after swapping :", num1)
print("Value of num2 after swapping :", num2)