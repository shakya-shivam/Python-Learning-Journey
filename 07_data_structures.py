# In this file, we will learn about inbuilt data structures in Python.


# Data structures are a type of storage in which we can store multiple values.
# There are four types of inbuilt data structures in Python.
# 01: List
# 02: Tuple
# 03: Set
# 04: Dictionary

# ==============================================
## 01:                 List
# ============================================== 

# When we want to store multiple values in a variable, we use a list.
# We will use square brackets '[]' to store values in a list.


# List supports indexing and slicing, similar to strings.

l1 = [1, 2, 3, 4, 5]

print(l1[0:3:1]) # Here, I am slicing a part [1, 2, 3] of a list.


# List has heterogeneous nature, we can store multiple data types.

l2 = [6, 6.5, 7j, True, str()]

print(l2) # Here, I am printing a list storing multiple data types.


# List has mutable nature, we can change anything.

l3 = [8, 9, 10, 11.1, 12]

l3[3] = 11 # Here, I am changing 11.1 to 11 easily.

print(l3) # Here, I am printing the modified list.


# List can also store duplicates.

l4 = [13, 13, 13, 14, 14, 14]

print(l4) # Here, I am printing a list with duplicate values.
 

## Reference copy, Shallow copy and Deep copy.


# Reference copy -
# In this, we simply provide two different names of same list.

l5 = [15, 16, 17, 18, 19, 20]

l6 = l5 # Here, I am providing second name of same list.

l6[0] = 150 # Here, I am converting value in second list.
# But it also reflects in the first list.

print(l6) # Here, I am printing second list.
print(l5) # Here, I am printing first list.


# Shallow copy -
# In this, we copy first list into second list.

l7 = [21, 22, 23, 24, 25]

l8 = l7.copy() # Here, I am copying first list into second list.

l8[0] = 210 # Here, I am changing 21 to 210 in second list 
# But it does not reflect in first list, this does not work on nested list.

print(l8) # Here, I am printing second list.
print(l7) # Here, I am printing first list.


# Deep copy -
# In this, we deeply copy first list into second list.

import copy

l9 = [26, 27, 28, [29, 30]]

l10 = copy.deepcopy(l9) # Here, I am deep copying the first list into the second list.

l10[3][1] = 300 # Here, I am changing inner list 30 to 300.

print(l10) # Here, I am printing second list.
print(l9)  # Here, I am printing first list.


# List Traversing -
# There are two types of traversing -
# 01: Direct traversing
# 02: Index traversing

# 01: Direct traversing -
# In this, we directly traverse on a list.

l11 = [31, 32, 33, 34, 35]

for i in l11: # Here, I am directly traversing on a list.
    print(i) # Here, I am printing values.


# 02: Index traversing -
# In this, we use index to traverse on a list.

l12 = [36, 37, 38, 39, 40]

for i in range(len(l12)): # Here, I am using len() function to 
                          # traverse on a list with index.
    print(l12[i]) # Here, I am printing values.


# List methods -
# Here are six of the most commonly used inbuilt methods in a list.

# 01: append()
# 02: insert()
# 03: pop()
# 04: remove()
# 05: extend()
# 06: sort()


# 01: append() -
# This adds a new item to the end of the list.

l13 = [41, 42, 43, 44]

l13.append(45) # Here, I am adding 45 to the list l13.

print(l13) # Here, I am printing the values.


# 02: insert() -
# This adds an item at a specific index.

l14 = [46, 47, 49, 50]

l14.insert(2, 48) # Here, I am adding 48 at index 2 of the list.

print(l14) # Here, I am printing the values.


# 03: pop() - 
# This removes last value from the list and returns it,
# if you provide index it will remove that specific value.

l15 = [51, 52, 53, 53.5, 54, 55]

l15.pop() # Here, I am removing a value from list.
rem_value = l15.pop(3) # Here, I am removing and saving 53.5 using index.

print(l15) # Here, I am printing list value.
print(rem_value) # Here, I am printing removed value.


# 04: remove() -
# This removes the first occurrence of the value from the list.

l16 = [56, 57, 60, 58, 59, 60]

l16.remove(60) # Here, I am removing the first occurrence of 60.

print(l16) # Here, I am printing values.


# 05: extend() -
# This adds a new list to the end of the existing list.

l17 = [61, 62, 63]
l18 = [64, 65]

l17.extend(l18) # Here, I am extending l17 with l18.

print(l17) # Here, I am printing the combined list values.


# 06: sort() -
# This will set the list items in ascending or descending order.

l19 = [69, 67, 70, 66, 68]

l19.sort() # Here, I am sorting the list in ascending order.

print(l19) # Here, I am printing list values.


l20 = [75, 72, 74, 71, 73]

l20.sort(reverse=True) # Here, I am sorting the list in descending order.

print(l20) # Here, I am printing list values.


# ==============================================
## 02:              Tuple
# ==============================================

# Tuple is also used to store multiple values and data types.
# We will use parenthesis '()' to store values in Tuple.
# Tuple can store duplicate values.
# Indexing and slicing are also similar to List.
# Tuple has heterogeneous nature also, so we can store anything.
# But tuples are immutable in nature, so we cannot change anything after creation.


## Tuple unpacking -
# 

a, b, c = (1, 2, 3) # Here, I am unpacking this tuple
# 'a' will hold 1 , 'b' will hold 2 and 'c' will hold 3

print(a) # Here, I am printing 'a'
print(b) # Here, I am printing 'b'
print(c) # Here, I am printing 'c'


## Tuple traversing -
# Tuples have two types of traversing methods similar to list.


# 01: Direct traversing -
# In this, we will directly traverse on a Tuple.

t1 = [5, 6, 7, 8, 9, 10]

for i in t1: # Here, I am traversing on tuple directly.
    print(i) # Here, I am printing tuple value.


# 02: Index traversing -
# In this, we will use index to traverse on a Tuple.

t2 = (11, 12, 13, 14, 15)

for i in range(len(t2)): # Here, I am traversing on tuple using the index.
    print(t2[i]) # Here, I am printing tuple value.


# The "Single Element" Trap -
# Always remember: to create a single-element tuple, add a comma ',' at the end.

t3 = (16) # Here, It seems like tuple but it is an integer.
t4 = (17,) # Here, It is the actual single element tuple.

print(t3) # Here, I am printing the integer.
print(t4) # Here, I am printing the single element tuple.


# Tuple Methods - 
# There are only two types of methods in tuple.


# 01: count() -
# This tells, How many times a specific value comes in a tuple.

t5 = (18, 19, 19, 19, 20)

value = t5.count(19) # Here, I am checking how many times 19 occurs in a tuple.

print(value) # Here, I am printing the number of how many times 19 occurs.


# 02: index()
# This returns the first index where a specific value occurs in a tuple.

t6 = (21, 22, 23, 24, 25)

ind = t6.index(22) # Here, I am checking the index of 22 in a tuple.

print(ind) # Here, I am printing the index value of 22 in a tuple.


# ==============================================
## 03:              Set
# ==============================================

# Set is also used to store multiple values.
# To create a set, we use curly braces '{}'. But in an empty condition,
# It is considered as a Dictionary.
# You can write duplicates, But when you run the file Python automatically
# Delete duplicate values from set.
# Sets do not support indexing, so we cannot access elements by index.
# Set is mutable, but we will use methods to remove or add any value.


# Set Methods -

# 01: add() -
# We use this to add a new item to the set.

s1 = {1, 2, 3, 4}

s1.add(5) # Here, I am adding 5 into set.

print(s1) # Here, I am printing set.


# 02: remove() and discard() -
# Both work same, we will use them to remove any element from the set.
# But 'remove()' raises an error if element does not exist in set,
# at the same time, 'discard()' does not raise any error.

s2 = {6, 7, 8, 9, 10}

s2.remove(10) # Here, I am removing 10 using 'remove()' method.
s2.discard(10) # Here, I am removing 10 using 'discard()' method.

print(s2) # Here, I am printing set.


# 03: union() -
# We use this to merge two sets, and this also removes duplicates from
# the new set. 


s3 = {11, 12, 13, 14, 15, 16}
s4 = {15, 16, 17, 18, 19, 20}

new_set = s3.union(s4) # Here, I am merging two sets.

print(new_set) # Here, I am printing 'new_set'.


# 04: intersection() -
# We use this, to extract common items in both sets.

s5 = {21, 22, 23, 24, 25, 26}
s6 = {25, 26, 27, 28, 29, 30}

common_items = s5.intersection(s6) # Here, I am extracting common items.

print(common_items) # Here, I am printing common items.


# 05: difference() -
# We use this, to extract items that are in the first set, 
# But not in the second.

s7 = {31, 32, 33, 34, 35}
s8 = {31, 32}

unique_items = s7.difference(s8) # Here, I am extracting unique items.

print(unique_items) # Here, I am printing 'unique_items' from set.


# ==============================================
## 04:             Dictionary
# ==============================================

# Dictionary is also used to store multiple values, but unlike set,
# It stores data in key-value pairs.
# We use curly braces '{}' to denote a dictionary. It is unordered in 
# older Python versions (before 3.7), but in modern Python they maintain
# insertion order.
# Dictionaries are mutable, which means we can change, add or remove items
# after creation.
# Dictionaries do not allow duplicate keys, but values can be duplicated.


## Dictionary Traversing -
# There are three most used types of traversing -


# 01: Keys -
# We use this to traverse only the keys of the Dictionary.

d1 = {'a': 1, 'b': 2, 'c': 3}

for k in d1.keys(): # Here, I am accessing keys of Dictionary.
    print(k) # Here, I am printing keys of Dictionary.

for i in d1: # Here, this works the same as 'd1.keys()'
    print(i) # Here, I am printing same keys of Dictionary.


# 02: Values -
# We use this to traverse only the values of the Dictionary.

d2 = {'d': 4, 'e': 5, 'f': 6}

for v in d2.values(): # Here, I am accessing values of Dictionary.
    print(v) # Here, I am printing values of Dictionary.


# 03: Items -
# We use this to traverse on both keys and values of the Dictionary.

d3 = {'g': 7, 'h': 8, 'i': 9}

for k, v in d3.items(): # Here, I am accessing both keys and values.
    print(f"Keys: {k}") # Here, I am printing keys only.
    print(f"Values: {v}") # Here, I am printing values only.


## Distionary Methods -

# 01: Get -
# We use this to access specific values using a key.

d4 = {'j': 10, 'k': 11, 'l': 12}

print(d4.get('k')) # Here, I am accessing value and printing at the same time.


# 02: Update -
# We use this to merge two dictionaries.

d5 = {'m': 13, 'n': 14, 'o': 15}
d6 = {'p': 16, 'q': 17, 'r': 18}

d5.update(d6) # Here, I am merging d6 to d5.
d5['z'] = 100 # Here, I am adding a new key-value pair directly.

print(d5) # Here, I am printing d5 merged with d6.


# 03: Pop -
# We use this to remove a specific value using its key.

d7 = {'s': 19, 't': 20, 'u': 21}

print(d7.pop('t')) # Here, I am popping and printing popped element.
print(d7) # Here, I am printing dictionary.


# =======================================================
# 🤖 AI TRANSPARENCY NOTE (Building in Public)
# =======================================================
"""
Transparency is a core part of my learning journey.
All logic, manual implementations, and practical code in this file were 
written and executed by me to build a deep understanding of Python data structures.

I actively use AI as my 'Pair Programmer' to:
- Review code against PEP 8 style guidelines.
- Audit English grammar and phrasing across comments and documentation.
- Discuss under-the-hood memory concepts (e.g., mutable vs. immutable, hashing,
  shallow vs. deep copy).

AI is an assistant to sharpen my understanding, not a replacement for my logic.
"""