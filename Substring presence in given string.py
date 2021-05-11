# The find() method finds the first element of the specified value.
# The find() methods returns -1 if the value is not found.

str="Welcome to python programming"
sub_str = "python"

print(str.find(sub_str))  #Position according to index.

if (str.find(sub_str) == -1):
    print("Not found")
else:
    print("Found")