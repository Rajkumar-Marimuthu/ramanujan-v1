# In Python, variables are created when you assign a value to it:
# Python has no command for declaring a variable.
# Variables are containers for storing data values.
x = 5
y = "Hello, World!"
print(x)
print(y)

# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type:	str
x = "Hello World"
x = str("Hello World")

# Numeric Types:	int, float, complex
x = 20
x = int(20)
x = 20.5
x = float(20.5)
x = 1j
x = complex(1j)

# Sequence Types:	list, tuple, range
x = ["apple", "banana", "cherry"]  # list
x = list(("apple", "banana", "cherry"))
x = ("apple", "banana", "cherry")  # tuple
x = tuple(("apple", "banana", "cherry"))
x = range(6)  # range

# Mapping Type:	dict
x = {"name": "John", "age": 36}  # dict
x = dict(name="John", age=36)

# Set Types:	set, frozenset
x = {"apple", "banana", "cherry"}  # set
x = set(("apple", "banana", "cherry"))

x = frozenset({"apple", "banana", "cherry"})  # frozenset

# Boolean Type:	bool
x = True
x = bool(5)

# Binary Types:	bytes, bytearray, memoryview
x = b"Hello"  # bytes
x = bytes(5)
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview

# None Type:	NoneType
x = None

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# casting - If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# get the type - You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'
print(x)

"""
Python ignores string literals that are not assigned to a variable, you can add a multiline string
(triple quotes) in your code and place your comment inside it
"""

myAddr = """
chennai
India
"""
print(myAddr)

# Variable names are case-sensitive.
# These are two different variables
a = 4
A = "Sally"

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
# Make sure the number of variables matches the number of values, or else you will get an error.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# The Python print() function is often used to output variables.
# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator,
# Python will give you an error:
x = 5
y = "John"

# print(x + y)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# The best way to output multiple variables in the print() function is to separate them with commas,
# which even support different data types:
print(x, y)

# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()


# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local,
# and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
