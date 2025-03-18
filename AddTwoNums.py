#Add Two Numbers in Python
#Author: Zhou Yiwen
#Using the + Operator
a = 15
b = 12
#Adding two numbers
res = a + b
print(res)

#Add Two Numbers in Python
#Author: Zhou Yiwen
#Using user input

#taking user input
a = input("First number:")
b = input("Second number:")

#converting input to float and adding
res = float(a) + float(b)
print(res)

#Add Two Numbers in Python
#Author: Zhou Yiwen
#Using a function

#function to add two numbers
def add(a,b):
 #converting input to float and adding
 result = float(a) + float(b)
 return result

#taking user input
a = input("First number:")
b = input("Second number:")

#calling function
res = add(a,b)
print("The answer is:")
print(res)
