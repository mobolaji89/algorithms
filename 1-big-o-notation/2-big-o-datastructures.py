# Big O for Python Data Structures

# Lists

"""
In Python lists act as dynamic arrays and support a number of common operations
through methods called on them. The most two common operations performed on a
list are indexing and assigning to an index position. These operations are
both designed to be run in constant time, O(1).

It is important to keep these factors in mind when writing efficient code.
More importantly begin thinking about how we are able to index with O(1).
"""

def method1():
    l = []
    for n in range(10000):
        l = l + [n]

def method2():
    l = []
    for n in range(10000):
        l.append(n)

def method3():
    l = [n for n in range(10000)]

def method4():
    l = list(range(10000))

"""
Results:

10 loops, best of 3: 162 ms per loop
1000 loops, best of 3: 820 µs per loop
1000 loops, best of 3: 307 µs per loop
10000 loops, best of 3: 77.7 µs per loop

The most effective method is the built-in range() function in Python!

It is important to keep these factors in mind when writing efficient code.
More importantly begin thinking about how we are able to index with O(1).
"""

# Dictionaries

# Dictionaries in Python are an implementation of a hash table. 
# They operate with keys and values, for example:

dict = {'a1':1, 'a2':2}

print(dict['a1']) #1

"""
Getting and setting items in a dictionary are O(1). Hash tables are designed
with efficiency in mind.
"""
