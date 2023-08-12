# In Python, variables are created when you assign a value to it:
# Python has no command for declaring a variable.
# Variables are containers for storing data values.
x = 5
y = "Hello, World!"
print(x)
print(y)

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





