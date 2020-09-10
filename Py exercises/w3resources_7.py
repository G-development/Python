#Write a Python program to accept a filename from the user and print the extension of that

fileName = input("Insert the name of a file: ")
fileName = fileName.split(".")
print("The extension of the file is: " + repr(fileName[-1]))