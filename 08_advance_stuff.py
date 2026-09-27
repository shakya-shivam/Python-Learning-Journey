# In this file, we will learn about Lambda expressions, Map, Filter, Zip,
# Comprehensions, Generators, and Decorators.


## Lambda expression -
# We use this to write concise code; it allows us to create anonymous functions in Python.

add = lambda a, b: a + b # Here, I am creating a function to add two values.
print(add(12, 8)) # Here, I am calling the function and printing the sum of 12 and 8.


## Map -
# We use this to apply a function to every item in an iterable and return an iterator.
# This works with both lambda expressions and normal functions.

num_list = [1, 2, 3, 4, 5]
final_list = list(map(lambda x: x ** 2, num_list)) # Here, I am squaring our list and generating a new list.
print(final_list) # Here, I am printing 'final_list'.



## Filter -
# We use this to filter items from an iterable based on a condition.

l1 = [6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, l1)) # Here, I am filtering even numbers from a list.
print(even) # Here, I am printing the new list (even) of even numbers.


## Zip -
# We use this to combine iterables into pairs of elements.

names = ["Shivam", "Rohan", "Rahul"]
ages = [22, 24, 23]
d = dict(zip(names, ages)) # Here, I am creating a dictionary using two lists. 
print(d) # Here, I am printing the dictionary (d).


## Comprehensions -
# Common comprehensions covered here: List, Dictionary, and Set.


## 01: List Comprehension -
# We use this to shorten our code.

l2 = [11, 12, 13, 14, 15]
l3 = [i for i in l2 if i % 2 == 0] # Here, I am extracting even numbers using list comprehension.
print(l3) # Here, I am printing the new list (l3).


## Dictionary Comprehension -
# We use this to shorten our code.

l4 = [16, 17, 18, 19, 20]
d1 = {i: i ** 2 for i in l4 if i % 2 == 0} # Here, I am creating a dictionary of squares for even numbers.
print(d1) # Here, I am printing the new dictionary (d1).


## Set Comprehension -
# We use this to shorten our code and automatically remove duplicate items.

l5 = [1, 2, 2, 3, 4, 4, 5, 5, 6] # Notice the duplicate numbers

s1 = {x ** 2 for x in l5 if x % 2 == 0} # Here, I am extracting unique squares of
# even numbers using set comprehension.

print(s1) # Here, I am printing the new set (s1). 
# Note: Sets are unordered, so output order may vary.


## Generators -
# We use this to save our memory.
# Let's see how it works.

def simple_function(): # Here, I am creating a simple function.
    for i in range(1, 11): # Here, I am selecting range from 1 to 10.
        return i # Here, I am returning that range, but 
                 # 'return' immediately exits the function after the first iteration.
    

sim_fun = simple_function() # Here, I am storing the returned value in a variable.
print(sim_fun) # Here, I am printing the stored return value (sim_fun).


def generator_function(): # Here, I am creating a generator function.
    for i in range(1, 11): # Here, I am setting up a range from 1 to 10.
        yield i # Here, 'yield' turns this function into a generator.
                # 'yield' pauses the function and preserves its state.
                # 'next()' resumes execution and fetches the next value on demand.


gen_fun = generator_function() # Here, I am again saving function (generator_function)
                               # in variable.
print(next(gen_fun)) # Here, calling next(gen_fun) prints 1.
print(next(gen_fun)) # Here, calling it again prints 2.


# Pro Tip: (x for x in range(5)) creates a Generator, NOT a tuple.
# To make a tuple, use tuple(x for x in range(5))


## Decorators -
# We use decorators to extend the behavior of a function without modifying it directly.

def decorator_func(func): # Here, I am creating a decorator that accepts a function as an argument.
    def wrapper(): # Here, I am creating a wrapper function to add extra behavior.
        # Note: In production, use *args, **kwargs inside wrapper to handle functions with arguments.
        print("Good Morning") # Here, I am adding behavior BEFORE the original function runs.
        
        func() # Here, I am calling our main/original function.
        
        print("Sir / Ma'am!\n") # Here, I am adding behavior AFTER the original function runs.
        
    return wrapper # Here, I am returning the wrapper function.

@decorator_func # Here, I am applying the decorator to the 'hello' function below.
def hello():
    print("Hello")

hello() # Here, I am calling the decorated function.


# =======================================================
#     🤖 AI TRANSPARENCY NOTE (Building in Public)
# =======================================================
"""
Transparency is a core part of my learning journey.
All logic, advanced patterns, and implementations in this file were 
written and executed by me to build a strong foundation in Python internals.

I actively use AI as my 'Pair Programmer' to:
- Audit docstrings and comments for clear technical English.
- Review code against PEP 8 styling conventions.
- Discuss under-the-hood execution (e.g., iterator protocols, stack frames, state preservation in generators).

AI sharpens my engineering workflow; the execution and logic remain entirely mine.
"""