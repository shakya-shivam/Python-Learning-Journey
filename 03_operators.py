# In this file, we will learn about operators in Python.

# The main purpose of operators in Python is to perform multiple types of operations.
# Python also follows the 'BODMAS' rule.
# There are four types of operators -

# 01_Arithmetic operators
# 02_Assignment operators / Shorthand operators
# 03_Comparison operators
# 04_Logical operators

# =========================================================================
# 01                      "Arithmetic Operators"
# =========================================================================

# '+' (Addition), '-' (Subtraction), '*' (Multiplication), '/' (Division), '//' (Floor Division),
# '%' (Modulus), '**' (Exponentiation)
# These are some important arithmetic operators in Python.

# Arithmetic operators generally work with numeric values, except for '+' and '*' which also work with strings.
# To know more, see my previous 02_string_and_casting.py file for more understending.


## '+' (Addition)

# We use this operator for adding two or more numbers like -

num_1 = 12
num_2 = 24
print(num_1 + num_2) 


## '-' (Subtraction)

# We use this operator for subtracting two or more numbers like -

num_3 = 11
num_4 = 55
print(num_4 - num_3)


## '*' (Multiplication)

# We use this operator for multipling two or more numbers like -

num_5 = 15
num_6 = 5
print(num_5 * num_6)


## '/' (Division)

# We use this operator for dividing two or more numbers like -

num_7 = 8
num_8 = 2
print(num_7 / num_8)


## '//' (Floor Division)

# We use this operator for extracting the answer without decimals after floor division like -

num_9 = 13
num_10 = 3
print(num_9 // num_10)


## '%' (Modulus)

# We use this operator for extracting the remainder after division like -

num_11 = 25
num_12 = 4
print(num_11 % num_12)


## '**' (Exponentiation)

# We use this operator for doing the power operation between numbers like -

num_13 = 5
num_14 = 2
print(num_13 ** num_14)


# =========================================================================
# 02                     "Assignment Operators"
# =========================================================================

# '=' (Assignment), '+=' (Addition Assignment), '-=' (Subtraction Assignment), '*=' (Multiplication Assignment),
# '/=' (Division Assignment), '//=' (Floor Division Assignment), '%=' (Modulus Assignment),
# '**=' (Exponentation Assignment)
# These are some important assignment operators in Python.

# The Assignment operators are used to assign values to variables.


## '=' (Assignment)

# We use this operator for assigning value in variable like -

name = "Buddy" # Here '=' this operator assign "Byddy" this string into 'name' this variable.


## '+=' (Addition Assignment)

# We use this operator to add numbers and assign at the same time like -

num_15 = 90
num_15 += 10 # Here we add '10' with '90' and assign the answer to the same 'num_15' variable at the same time.
print(num_15)


## '-=' (Subtraction assignment)

# We use this operator to subtract numbers and assign at the same time like -

num_16 = 85
num_16 -= 5 # Here we subtract '5' with '85' and assign the answer to the same 'num_16' variable at the same time.
print(num_16)


## '*=' (Multiplication Assignment)

# We use this operartor to multiply numbers and assign at the same time like -

num_17 = 3
num_17 *= 2 # Here we multiply '2' with '3' and assign the answer to the same 'num_17' variable at the same time.
print(num_17)


## '/=' (Division Assignment)

# We use this operator to divide numbers and assign at the same time like -

num_18 = 10
num_18 /= 2 # Here we divide '10' by '2' and assign the answer to the same 'num_18' variable at the same time.
print(num_18)


## '//=' (Floor Division Assignment)

# We use this operator for extracting without decimal value and assign at same time like -

num_19 = 11
num_19 //= 2 # Here we floor divide '11' by '2' and assign the answer to the same 'num_19' variable at the same time.
print(num_19)


## '%=' (Modulus Assignment)

# We use this operator for extracting remainder and assign at same time like -

num_20 = 16
num_20 %= 3 # Here we extracting the remainder with mode between '16' and '3' and assign the answer to the same
            # 'num_20' variable at the same time.
print(num_20)


## '**=' (Exponentiation Assignment)

# We use this operator for doing power operation with numbers and assign at same time like -

num_21 = 10
num_21 **= 2 # Here we exponent '10' with '2' and assign the answer to the same 'num_21' variable at the same time.
print(num_21)


# =========================================================================
# 03                         "Comparison Operators"
# =========================================================================

# '==' (Equal To), '!=' (Not Equal To), '>' (Greater Than), '<' (Less Than), 
# '>=' (Greater Than or Equal To), '<=' (Less Than or Equal To)
# These are important comparison operators in Python.

# We use them to compare two values. They form the core of "Decision Making" 
# in programming (like if-else conditions).
# The result of a comparison operator is ALWAYS a boolean (True or False).


## '==' (Equal To)

# We use this operator to check if the value on the left is exactly equal to the right.

num_22 = 12
num_23 = 12
print(num_22 == num_23) # Here we compare two numeric values for equality.


## '!=' (Not Equal To)

# We use this operator to check if the values on both sides are different from each other.

num_24 = 14
num_25 = 14.1
print(num_24 != num_25) # Here we check if the two values are not equal.


## '>' (Greater Than)

# We use this operator to check if the left value is strictly greater than the right value.

num_26 = 33
num_27 = 44
print(num_26 > num_27) # Here we compare which numeric value is greater.


## '<' (Less Than)

# We use this operator to check if the left value is strictly less than the right value.
    
num_28 = 55
num_29 = 66
print(num_28 < num_29) # Here we compare which numeric value is less.


## '>=' (Greater Than or Equal To)

# We use this operator to check if the left value is greater than or equal to the right value.

num_30 = 88
num_31 = 77
print(num_30 >= num_31) # Here we compare which numeric value is greater or equal on both sides.


## '<=' (Less Than or Equal To)

# We use this operator to check if the left value is less than or equal to the right value.

num_32 = 100
num_33 = 101
print(num_32 <= num_33) # Here we compare which numeric value is less than or equal on both sides.

# =========================================================================
# 04                                "Logical Operators"
# =========================================================================

# 'and', 'or', 'not'
    
# We use logical operators to combine multiple conditions together. 
# They are the backbone of complex decision-making in Python. 
# Just like comparison operators, they always return boolean values (True or False).


## 'and' 

# We use this operator when we want ALL conditions to be True.
# It returns True ONLY if every single condition is True. 
# If even one condition is False, the whole result becomes False.

num_34 = 10
num_35 = 20
num_36 = 30
    
# Here we check if 10 is less than 20 AND 20 is less than 30.
print((num_34 < num_35) and (num_35 < num_36)) # This will print True.


## 'or'

# We use this operator when we want AT LEAST ONE condition to be True.
# It only returns False if ALL conditions are completely False.

num_37 = 40
num_38 = 50
num_39 = 60
    
# Here we check if 40 is greater than 50 (False) OR 50 is less than 60 (True).
print((num_37 > num_38) or (num_38 < num_39)) # This will print True.


## 'not'

# We use this operator to reverse the boolean result. 
# It simply turns True into False, and False into True.

num_40 = 100
num_41 = 200
    
# Normally, 100 < 200 is True, but 'not' will reverse the final answer.
print(not(num_40 < num_41)) # This will print False.


#                 ==========================================
#                      A QUICK NOTE ON VARIABLE NAMING
#                 ==========================================

# I am fully aware of PEP 8 standards and the importance of using 
# highly descriptive and context-driven variable names. 

# However, since this single file contains multiple practice snippets 
# for Operators, I intentionally used short variable names to avoid 
# naming collisions and overriding Python's built-in functions. 

# In real-world projects and modular code, I strictly stick to 
# relatable and professional naming conventions! 

#                  ====================================
#                       A QUICK NOTE ON AI USAGE:
#                  ====================================

# While 100% of the code, logic, and concepts in this file are written 
# and understood by me, I actively use an AI assistant to polish the 
# English grammar and formatting of my comments. 
# My primary focus right now is strictly on mastering Python logic! 