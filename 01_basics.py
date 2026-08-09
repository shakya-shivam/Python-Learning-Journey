# In this file, we will learn about 'Comments', 'Variables' and 'Data types'

# This is a single-line Comment, To create a single-line comment, we use "#"

"""
This is a multi-line Comment, To create a multi-line comment, we use triple quotes 
"""

#================================================================================================================

#                                   "VARIABLES AND DATA TYPE"

## Variables

# Variables work as storage in programming, So simply, variables can store data.

# 01 => Don't use numbers at the start of the variable names; you can use them at the end.
# 02 => Don't use spaces in variables.
# 03 => Don't use any special characters in variables except _ .

name = "Buddy"  #Data type = "String, (str)"
age = 22        #Data type = "Integer (int)"
salary = 1.5    #Data type = "Float (float)"
day = True      #Data type = "Boolean (bool)"

## Naming convention in Variables

buddySalary = 1.5  #Camel Case
BuddySalary = 1.5  #Pascal Case
buddy_salary = 1.5 #Snake Case

# You can use any type in Python.

## Data type explanation

# Numbers - There are three types of numeric values. 
# 01 => Integer contains (infinity,-3,-2,-1,0,1,2,3,infinity)
# 02 => Float contains decimal values (1.2,13.9,12.5)
# 03 => Complex contains imeginary values (12j,15j)

# String 
# It contains Characters, Numbers, Special Characters and Everything.

# Booleon
# It returns True and False only.

#======================================================================================================================

#                               "OUTPUT AND DATA TYPE VERIFICATION"

# Printing the values to see them in the terminal
print("Robot Name:", name)
print("Robot Age:", age)
print("Salary Assigned:", salary)
print("Is it Day:", day)

# Checking the actual data types using type() function.
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of salary:", type(salary))
print("Type of Day:", type(day))