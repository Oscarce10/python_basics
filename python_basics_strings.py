# Can use double or single quotes
print("Hello World")
print('Hello Python')
print("--------------------------------------------------------")

# Strings are arrays but in Python doesn't exist char type it is just a string with a lenght of 1
a = "Hello world!"
print(a[0])
print("--------------------------------------------------------")

# To print a range we use colon
print(a[1:4])
print("--------------------------------------------------------")

# If we use negative indexes it starts from the end to the beginning
print(a[-5])
print(a[-5:-2])
print("--------------------------------------------------------")

# Length of a string can be calculated with len()
f = len(a)
print(f)
print("--------------------------------------------------------")

# .lower() to return lowercase
print("HELLO WORLD".lower())
print("--------------------------------------------------------")

# .upper() to return uppercase
print(a.upper())
print("--------------------------------------------------------")

# .replace() replace a string with another one
print(a.replace("world", "python"))
print("--------------------------------------------------------")

# .split() splits the string into substrings if it finds instances of the separator
a = a.split(" ")
print(a[0])
print("--------------------------------------------------------")

# Check string
# Check if phrase ell is in the text
x = "ell" in a[0]
print(x)
print("--------------------------------------------------------")

# Check if the phrase ell is not in the text
x = "ell" not in a[0]
print(x)
print("--------------------------------------------------------")

# String format
age = 22
name = "Oscar"
# We can combine strings and numbers by using the format() method and can send arguments with {}
print("Hello, my name is {} and I'm {} years old".format(name, age))

# Also we can assign numbers to placeholders to give order
print("Hello, my name is {1} and I'm {0} years old!".format(age, name))
print("--------------------------------------------------------")