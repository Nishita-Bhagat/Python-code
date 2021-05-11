#Approach 1 :
    # 1) Find the reverse of string
    # 2) Check if reverse and original are same or not

s = input("Enter a string:") #abcdefgh
revstr = (s[::-1])   #hgfedcba reverse order

if revstr == s:
    print("Palindrome")
else:
    print("Not palindrome")
