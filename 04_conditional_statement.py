# In this file, we will learn about conditional statements in Python.

# 'if', 'elif', and 'else' are the three main conditional statements in Python.
# We often use them together to handle multiple conditions.

# Note:-

# We only provide conditions for 'if' and 'elif'.
# The 'else' block catches everything else.
# It is crucial to remember that we must use proper indentation inside these blocks.
# We use the 'pass' keyword when we want to leave a block empty without getting an error.
# Remember, 'else' is the final block and it does not accept any conditions.

# Let's look at a practical example.

# Example Question:-

# Q_01: Write a Python program to check if a user is eligible to vote?

# To solve this, we will first take the age as input from the user. 
# Then, we will check if the age is greater than or equal to 18.

age = int(input("What is your age? :- ")) # Here, I am using type casting to convert 
# the input string into an integer.

if age >= 18: # Here, we check if the age is actually greater than or equal to 18.
    print("You are a valid voter.")
else:
    print("You are not a valid voter.")


# Q_02: Write a Python program to check if the number is even or odd using 'Ternary Operator'?

# To solve this, we will first take a number as input from the user.
# Then, we will check if the number is even or odd using the ternary operator.

num = int(input("Enter the number you want to check :- ")) # Here, I am using type casting
# to convert the input string into an integer.

print("even") if num % 2 == 0 else print("odd") # Here, we check if the number is actually even or odd.


# Q_03: Write a Python program to check which is the largest variable of them using if, elif ladder -
#       'a = 12', 'b = 24' and 'c = 20'

# To solve this, we will take three variables and check which one is the largest
# using an if, elif ladder.

a = 12
b = 24
c = 20

if a > b and a > c: # Here, I am checking if 'a' is actually greater than both 'b' and 'c'.
    print("'a' is the largest variable.")
elif b > a and b > c: # Here, I am checking if 'b' is actually greater than both 'a' and 'c'.
    print("'b' is the largest variable.")
else: # Because the 'else' block does not accept any conditions, I am using it for the last remaining variable.
    print("'c' is the largest variable.")


# =====================================================================
#                 A QUICK NOTE ON AI USAGE:
# =====================================================================

# While 100% of the code, logic, and concepts in this file are written 
# and understood by me, I actively use an AI assistant to polish the 
# English grammar and formatting of my comments. 
# My primary focus right now is strictly on mastering Python logic! 
