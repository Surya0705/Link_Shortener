import pyshorteners # Importing the pyshortener module for shortening urls.

a = input("Enter the Link:") # Taking the link as input from user.
b = pyshorteners.Shortener() # Defining the function.
c = b.tinyurl.short(a) # Shortening the link.
print(c) # Printing the Shortened link.