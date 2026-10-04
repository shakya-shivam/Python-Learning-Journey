# In this file, we will learn about exceptions and file handling in Python.


# ====================================================================
##                  Exception Handling
# ====================================================================

"""
Exceptions are raised when the program is syntactically
correct, but the code results in an error. This error does not
stop the execution of the program, however, it changes the
normal flow of the program.

Syntax errors cannot be handled using try-except blocks; 
only runtime exceptions can be handled.
"""


## 01: Basic try and except -
# Try: Tests a block of code for errors.
# Except: Catches and handles the exception if one occurs.
# Custom Exceptions or Universal Catcher.

try:
    a = 12
    b = 0

    print(a / b)  
except Exception as e: # Here, I am catching the error to maintain our code flow.
    print(f"\nError: {e} !!\n") # Here, I am printing the error.

print(a + b) 


## 02: The else Block -
# Else- Executes only if no exception occurs in the try block.
try:
    c = 10
    d = 5

    print(c / d)
except Exception as e: # Here, I am catching the error to maintain our code flow.
    print(f"\nError: {e} !!\n") # Here, I am printing the error.
else: # Here, This will run if try block does not catch any error.
    print("\nCode Run Successfully.\n")

print(c + d)


## 03: The finally Block -
# Finally- This will definitely run no matter what happens.

try:
    e = int(input("Provide number here :- "))
    f = int(input("Provide number here :- "))

    print(e / f)
    print(e + f)
except Exception as err: # Here, I am catching the error to maintain our code flow.
    print(f"\nError: {err} !!\n") # Here, I am printing the error.
finally:
    print("\n\nHello Friends I am the Boss\n\n")




## 04: The raise Keyword (Custom Exceptions) -
# Raise- Raises a custom error as you need.
try:
    age = int(input("Enter your age here :- "))

    if age < 18: # Here, I am checking if user is 18+ or not.
        raise Exception("You must be 18+") # Here, I am raising an error if user is not 18+.
    print("Access Granted")
except Exception as e: # Here, I am catching the error to maintain our code flow.
    print(f"\nError: {e} !!\n") # Here, I am printing the error.



# ====================================================================
##                      File Handling
# ====================================================================

"""
File handling in python, as the name suggests it deals with
files with python.
That means creating, reading, updating and deleting (CRUD)
operations in different files.
"""


## 05: The open() Function & Modes -

# To open a file, we use the open() function. It accepts two parameters:
# 1. Location/path of the file, 
# 2. Mode of operation ("r", "w", "a", "x").

## "r": For reading the file. Error if file does not exist.
# open('location', 'r') # This is the syntax.

## "w": Overwriting the file. Creates if it does not exist.
# open('location', 'w') # This is the syntax.

## "a": For appending content in the file. Creates if it does not exist.
# open('location', 'a') # This is the syntax.

## "x": Create a file. Error if file already exists.
# open('location', 'x') # This is the syntax.


## 06: The with open() Magic (Context Manager) -

# The 'with' statement acts as a context manager,
# automatically closing the file once execution completes.

with open('01_basics.py', 'r') as fs: # Here, I am reading my previous file.
    print(fs.read())


# Writing to a file using context manager
with open('sample.txt', 'w') as file:
    file.write("Hello, this is a test write operation.\n")


# =======================================================
#     🤖 AI TRANSPARENCY NOTE (Building in Public)
# =======================================================
"""
Transparency is a core part of my learning journey.
All logic, manual implementations, and architectural flow in this file 
were created and executed by me to master Python error handling and I/O operations.

I actively use AI as my 'Pair Programmer' to:
- Audit docstrings, comments, and phrasing for clear technical English.
- Review code against PEP 8 formatting standards.
- Discuss edge cases (e.g., custom exceptions, resource leakage, context managers).

AI is a tool to refine my developer communication; the execution and understanding
remain entirely mine.
"""
