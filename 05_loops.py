# In this file we will learn about loops in Python.

# =====================================================================
# --- Common Control Statements for BOTH 'for' and 'while' loops ---
# =====================================================================

# 1. 'break': We use this to immediately exit the loop entirely, 
#    even if the loop hasn't finished its full cycle.

# 2. 'continue': We use this to skip the rest of the current iteration 
#    and jump directly to the next iteration of the loop.

# 3. 'else' with a loop (A special Python feature): 
#    The 'else' block runs ONLY if the loop finishes its complete cycle naturally. 
#    Note: If the loop is forcefully stopped by a 'break' statement, 
#    the 'else' block will NOT run.

# When we perform repetitive tasks, we use loops.
# There are two main types of loops in Python:
# 01:- for loop    02:- while loop


## 01:- for loop -

# We use a 'for' loop when we know exactly how many times we need to iterate.
# In a 'for' loop, we often use the range() function. Python asks
# us for three arguments: start point, stop point, and step.
# The most important thing is that the stop point is exclusive (stop - 1).
# This means if we give 10 as the stop point, Python will only run up to 9.
# We must always keep this in mind for our code to work properly.

# Let's solve some questions for better understanding.


# Q_01: Write a Python program to print numbers from 1 to 10?

for i in range(1, 11, 1): # Here, I am using the start, stop, and step approach.
    print(i) # Here, I am printing 'i' because it takes each number one by one from the range.


# Q_02: Write a Python program to find the numbers which are divisible by 3 between the range of 100 to 500?

for i in range(100, 501, 1): # Here, I set the stop point to 501 because it is always exclusive (-1).
    if i % 3 == 0: # Here, I am checking if the number is completely divisible by 3.
        print(i)


## 02:- while loop -

# We use a 'while' loop when we don't know exactly how many times
# the loop needs to run, but we know the condition that must be met.
# A 'while' loop keeps executing as long as its condition remains True.

# Unlike a 'for' loop which uses the range() function, a 'while' loop
# depends on three essential steps to work perfectly:
# 1. Initialization: Setting a starting value for a variable before the loop.
# 2. Condition: The rule checking if the loop should continue running.
# 3. Increment/Decrement: Updating the variable inside the loop.

# WARNING: If we forget the 3rd step (Increment/Decrement), the condition
# will never become False. This causes an 'Infinite Loop' and crashes the program.

# Let's solve some questions for better understanding.


# Q_03: Write a Python program to take a number as input from the user 
# and reverse it using a 'while' loop?

num = int(input("Which number do you want to reverse? :- "))
r_num = 0 # This variable will store our reversed number.

while num > 0:
    d_value = num % 10       # Step 1: Get the last digit of the number.
    num = num // 10          # Step 2: Remove that last digit from the original number.
    r_num *= 10              # Step 3: Shift the existing digits in r_num to the left.
    r_num += d_value         # Step 4: Add the extracted last digit to r_num.

print(f"The reversed number is: {r_num}") # Using f-string for a cleaner output!


# =====================================================================
#                      A QUICK NOTE ON AI USAGE:
# =====================================================================
# While 100% of the code, logic, and concepts in this file are written 
# and understood by me, I actively use an AI assistant to polish the 
# English grammar and formatting of my comments. 
# My primary focus right now is strictly on mastering Python logic! 