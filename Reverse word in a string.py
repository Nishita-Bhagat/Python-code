str="Welcome to python programming"

words=str.split(" ")
print(words)   #['Welcome', 'to', 'python', 'programming']

words=words[-1::-1]
print(words)  #['programming', 'python', 'to', 'Welcome']

outputstr=' '.join(words)
print(outputstr)
