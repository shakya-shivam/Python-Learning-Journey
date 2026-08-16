# In this file, we will learn about 'String', 'inputs' and 'Type Casting'

#=======================================================================================================

#                                  "STRING"

## String Indexing

# Very important and most used.
# Immutable nature, you can't change the string's single character.
# Every string has its index.
# We use indexing to extract a specific part of a string.
# There are two types of indexing -

# 01 Positive Indexing -

# It always starts from '0', meaning the index of the first character is always '0'.
# exp
#    "Buddy"
#     01234

# 02 Negative Indexing -

# It always starts from '-1', meaning the index of the last character is always '-1'.
# exp
#    "B u d d y"
#    -5-4-3-2-1

# How to extract a single character from  a string -

a = "BUDDY"

print(a[0]) # For extracting 'B' 
print(a[4]) # For extracting 'Y'

## NOTE -> String indexing also applies to the spaces within a string.

## String Slicing

# String slicing is the process of extracting a portion of a string.
# It uses the syntax [start:stop:step]

# There are default values as well, such as:

# The start point is by default '0'.
# The stop point is by default the last index of the string. 
# The step is by default '1'.

## String Concatenation 

b = "Hello"
c = "Buddy"

print(a + b) # We use this to concatenate two strings together.

## String Repetition

d = "Buddy"

print(c * 2) # We use this to repeate the string.

## For more practice and terminal implementation.

e = "hello I am Data Scientist"

print(e[:5:])    # Extracting hello
print(e[11:15:]) # Extracting Data
print(e[16::])   # Extracting Scientist
print(e[::-1])   # Reverse the whole string 

##                                   "Print Statement Ways"

# In this section, we will look at:
# What is a formatted string?
# What are the escape sequences?
# What is a raw string?

# What is a formatted string - 

ai = "Buddy"

print(f"My personal ai assistant is {ai}") # To add variables in a single string we use formatted string.

# What are the escape sequences - \n, \b, \t etc.

# \n ends the line and starts a new one.
# \b acts as a backspace.
# \t adds a tab (multiple spaces).

# What is a raw string -

print(r"Hello how are you\n") #\n will not work now.

##                                  "Type Conversion"

# When we have to convert one datatype to another we use type conversion.

## int() -

# We can convert a data type into an int only if it contains a valid integer value.

f = "23" # Currently it's a string, but we can convert it into an int because it contains a valid number.
f = int(f)
print(f)

## float() -

# We can convert a data type into a float if it contains a valid number. 
# A float is essentially a number with a decimal point.
# exp -

# 23 We all know it's an integer, right?

# 23.0 This is a float because it has a decimal value. 
# That's why I say a float is a more detailed version of an int.

g = "35"
g = float(g)
print(g)

## str() -

# We all know that a string can hold almost anything, which is why we often use string conversion.
# We use it to  merge (concatenate) any data type with an existing string.

# exp -

h = "My age is "
age = 22
age = str(age) # To merge with string we use string conversion.
print(h + age)

## bool() -

# There are two concepts in bool - 
# Truthy values -> Almost everything is covered in truthy values.
# Falsy values -> 0 (Integer), 0.0 (Float), False (Boolean), "" (Empty String), [] (Empty List), 
# () (Empty Tuple), {} (Empty Dictionary), None.

# exp -

i = 23
i = bool(i) # We use this to convert any data type into True and False.
print(i)

##                                "Input Statement Ways"

# input() is a built-in function in Python. We use it to take input from the user.
# The default input type is always a string. We can take custom inputs (like ints) using type conversion.
# We can also pass a prompt message in this function for a better user experience.

# exp -

j = input("What is your name ? ")
print(f"My name is {j}") # We can also use 'f' string in the print function for better visuals.

k = int(input("What is your age ? "))
print(f"My age is {k}")

#                                   ==========================================
#                                        A QUICK NOTE ON VARIABLE NAMING
#                                   ==========================================

# I am fully aware of PEP 8 standards and the importance of using 
# highly descriptive and context-driven variable names. 

# However, since this single file contains multiple practice snippets 
# for Strings and Type Casting, I intentionally used random/short 
# variable names (like a, g, h) to avoid naming collisions and 
# overriding Python's built-in functions (like I experienced with 'str'). 

# In real-world projects and modular code, I strictly stick to 
# relatable and professional naming conventions! 

#                                    ====================================
#                                         A QUICK NOTE ON AI USAGE:
#                                    ====================================

# While 100% of the code, logic, and concepts in this file are written 
# and understood by me, I actively use an AI assistant to polish the 
# English grammar and formatting of my comments. 
# My primary focus right now is strictly on mastering Python logic! 
