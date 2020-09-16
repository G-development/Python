#Write a Python program which accepts a sequence of comma-separated numbers from user 
#and generate a list and a tuple with those numbers.

x = input("Insert numbers, separated with a comma: ")
list = x.split(",")
tuple = tuple(list)

print("The list is: " + str(list))
print("The tuple is: " + str(tuple))