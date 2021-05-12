# Input : Welcome
# Output : 7

# Method 1 : Using for loop
str="Welcome"  # 7
count = 0
for i in str:
    count = count+1
print(count)

# Method 2 : Using while loop and Slicing technique
str = "Welcome to my Kingdom" # 21
while str[count:]:
    count = count+1
print(count)

# Method 3 : Using built-in function len()
str = "Welcome Learners" # 16
print(len(str))

# Method 4 : Using join and count
str = "Good Morning"
random_str = "X"
print((random_str).join(str))  #GXoXoXdX XMXoXrXnXiXnXg
print((random_str).join(str).count(random_str)+1) # 12
