# Commentaries start with pound #

"This is a comment " \
"written in more than " \
"just one line"
"As long as the string is not assigned to a variable, " \
"Python will read the code, but then ignore it, and you have made a multiline comment."

# Variables - No declaration required
a = 3
b = "Hello world"
c = 'Variable with single quotes'

# Python lets assign the same value to multiple variables in one line:
x, y, z = 1, False, "word"
print(x,y,z)
print("--------------------------------------------------------")

# Concatenation is used with + sign if want to concat string with number cast number to str
print("Value of a: "+str(a)+"Value of y: "+str(y))
print("--------------------------------------------------------")


# A local variable can be used into a local environment without affecting global value
def fun():
    a = "1525"
    print("Variable local a: " + str(a))


fun()
print("Se imprime variable global de a modificada localmente: " + str(a))
print("--------------------------------------------------------")

# A global variable can be created inside a local environment by using the word global
def func():
    global a
    a = "De 3 se cambia a String"
    print(a)

func()
print("Se imprime variable a: " + a)
print("--------------------------------------------------------")


# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

# You can get the data type of any object by using the type() function:
print("Categories of data")
print("tipo de la variable a: ")
print(type(a))

print("tipo de la variable y: ")
print(type(y))
print("--------------------------------------------------------")


def cambioTipo():
    print("Changing type of data")
    x = 3j
    print("tipo de la variable x: ")
    print(type(x))

    x = {"name" : "John", "age" : 36}
    print("tipo de la variable x: ")
    print(type(x))

    x = memoryview(bytes(5))
    print("tipo de la variable x: ")
    print(type(x))
    print("--------------------------------------------------------")

cambioTipo()

# If you want to specify the data type, you can use the following constructor functions:
def assignType():
    print("Assigning type of data")
    x = int(20)
    print(type(x))
    x = list(("apple", "banana", "cherry"))
    print(type(x))
    x = bool(5)
    print(type(x))
    x = dict(name="John", age=36)
    print(type(x))
    print("--------------------------------------------------------")

assignType()


# Numbers in Python
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
def numbers():
    x = 700000000000
    print(x)
    x = -125000000
    print(x)

    f = 1.12548
    print(f)
    f = 125.24
    print(f)
    f = -0.0000000000000025
    print(f)
    print("--------------------------------------------------------")

numbers()

# Complex numbers are written with a "j" as the imaginary part:
def complex():
    f = 5+3j
    print(f)
    f = -3j
    print(f)
    f = 1j
    print(f)
    print("--------------------------------------------------------")

complex()

# Casting numbers
def convertNumber():
    x = 5
    y = 2.8
    z = 3 + 2j

    a = float(x)
    b = int(y)

    print(a)
    print(b)

    print(type(a))
    print(type(b))

convertNumber()