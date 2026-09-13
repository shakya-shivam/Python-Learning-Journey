# In this file, we will learn about functions in Python.
# (The core of modular coding)

# We use functions for code reusability in Python.
# A function in Python is a block of reusable code, 
# whenever we call it, it runs immediately.
# We also use functions for modularity, readability and easy debugging.


## PRINT vs RETURN

# PRINT: This is only used for showing code output on the terminal but,
# we can't use this data in any other calculation.

# RETURN: It throws the value outside from the function and we save that value
# in a variable and use in our code.

# Print example -

def show_addition(a, b):
    print(a + b)  # this only prints on the terminal.

# Return example -

def get_addition(a, b):
    return a + b  # this returns the value and we also save that value.

# we use returned value here.

final_value = get_addition(10, 20)
print(f"The returned value multiplied by 2 is: {final_value * 2}")


## ARGUMENTS/POSITIONAL vs KEYWORD ARGUMENTS

# Positional: We have to pass the value in the same sequence in which 
# the parameters were created.

# Keyword: We assign values using parameter names, so we don't need 
# to worry about the sequence.

def create_profile(name, age, device):
    print(f"Profile: {name}, Age: {age}, Uses: {device}")

# Positional Argument (sequence is always correct)
create_profile("Shivam", 24, "MacBook")

# Keyword Argument (don't need to worry about sequence)
create_profile(device="MacBook", name="Shivam", age=24)


## DEFAULT PARAMETERS

# If we don't provide a value at the time of function calling
# the function uses its own default value.

def greet_user(name="Guest"):
    print(f"Hello, {name}! Welcome to the system.")

greet_user("Shivam")  # output: Hello, Shivam!
greet_user()          # output: Hello, Guest! (because we didn't pass any name)


## PRACTICAL EXAMPLES (Real-world Logic)

def table_printing(x):
    """
    This function generates the table of any number.
    """
    print(f"\n--- Table of {x} ---")
    for i in range(1, 11):
        print(f"{x} * {i} = {x * i}")

def check_palindrome_number(x):
    """
    This function checks if a number is a palindrome with the help 
    of pure mathematical logic (while loop) .
    """
    copy_num = x
    rev_num = 0
    while x > 0:
        rev_num = (rev_num * 10) + (x % 10)
        x = x // 10
        
    if copy_num == rev_num:
        print(f"{copy_num} is a Palindromic Number.")
    else:
        print(f"{copy_num} is NOT a Palindromic Number.")

def check_palindrome_string(text):
    """
    This function checks if a string is a palindrome with the 
    help of Python string slicing.
    """
    rev_text = text[::-1]
    if text == rev_text:
        print(f"'{text}' is a Palindrome String.")
    else:
        print(f"'{text}' is NOT a Palindrome String.")

# --- Testing the Functions ---
# table_printing(12)
# check_palindrome_number(121)
# check_palindrome_string("naman")


# =======================================================
# 🤖 AI TRANSPARENCY NOTE (Building in Public)
# =======================================================
"""
Transparency is a core part of my learning journey. 
While the core logic, system design, and raw code in this file are completely 
my own, I actively use AI (Google Gemini) as my 'Pair Programmer'. 

I use AI to:
- Conduct code reviews and ensure PEP 8 compliance.
- Fix grammar and structure in my documentation/docstrings.
- Discuss system architecture and best practices.

AI is a tool to enhance my 'System Thinking', not a replacement for my logic.
"""