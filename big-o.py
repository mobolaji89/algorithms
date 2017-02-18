# Introduction to Algorithm Analysis and Big O

# Functions that take an input of n sum the numbers from 0 to n

# Function 1
def sum1(n):
    final_sum = 0

    for x in range(n+1):
        final_sum += x

    return final_sum

print(sum1(10)) #55

# Function 2
def sum2(n):
    return (n*(n+1))/2

print(sum2(10)) #55

"""
Function 2 is much more efficient, running at a much faster rate than the first.
However, we cannot use the amount of time it takes to run as an objective measurement,
because that will depend on the speed of the computer itself and hardware capabilities.
Therefore, we need to use Big O.

Big O Notation describes how quickly runtime will grow relative to the input,
as the input gets arbitrarily large.

Key Points:
    We want to compare how quickly runtime will grow, not compare exact runtimes,
    since those can vary depending on hardware.

    Since we want to compare for a variety of input sizes,
    we are only concerned with runtime grow relative to input.
    This is why we use N notation.

    As N gets arbitrarily large we only worry about terms that will grow the fastest,
    as N gets larger.
    Big-O analysis is also known as asymptotic analysis.

Analysis example:
    sum1(), above, can be said to be O(n) since its runtime grows linearly with input size.
"""


# Big O Examples ---------------------------------------------------------------

# O(1) Constant

arr = [1,2,3]

def func_constant(values):
    print(values[0])

func_constant(arr) #1

"""
This function is constant, because regardless of the array size,
it's only ever going to take one constant step size.
It will only ever print the first value from the array.
"""

# O(n) Linear

def func_linear(arr):

    for val in arr:
        print(val)

func_linear(arr)
"""
1
2
3
4
5
6
"""

"""
This function is linear because, the number of operations that takes place,
will scale linearly with N (array).
"""

# O(n^2) Quadratic

arr = [1,2,3]

def func_quadratic(arr):

    for x in arr:
        for y in arr:
            print(x, y)

func_quadratic(arr)
"""
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
"""

"""
This function has two loops, one nested inside the other.
This means for an array of N items, we will have to perform N operations
for every item in that list.
That means in total, we will perform N times N (n^2) actions.
"""


# Significant and Insignificant Terms --------------------------------------------

"""
When it comes to Big O notation we only care about the most significant terms.
As the input grows larger, only the fastest growing terms will matter.
"""

arr = [1,2,3]

# O(n) example

def print_1(arr):

    for val in arr:
        print(val)

print_1(arr)
"""
1
2
3
"""

# O(2n) example

def print_2(arr):

    for val in arr:
        print(val)

    for val in arr:
        print(val)

print_2(arr)
"""
1
2
3
1
2
3
"""

"""
If N is going to infinity, the constant (2 in the O(2n) example) can be dropped.
So in this case, both of the examples are O(n).
"""


# More complex Big O function example ------------------------------------------

arr = [1,2,3,4,5,6,7,8,9,10]

def comp(arr):

    print(arr[0]) # O(1)

    midpoint = int(len(arr)/2) # O(n) ... O(1/2 * n)

    for val in arr[:midpoint]:
        print(val)

    for x in range(10): # O(10)
        print('Hello World')

comp(arr)

"""
1
1
2
3
4
5
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
"""

"""
In total, when we add all the orders up we have:
    O(1 + n/2 + 10)

But we can simplify this equation, because 1 and 10 are insignificant,
and dividing N by 2, as N gets larger, will really not have much of an effect.
This simplifies the equation to:
    O(n)
"""


# Best case versus Worst case --------------------------------------------------

arr = [1,2,3,4,5]

def matcher(arr, match):

    for item in arr:
        if item == match:
            return True

    return False


# Best case:
print(matcher(arr, 1)) # True
# O(1), because the match is found at the first constant

# Worst case:
print(matcher(arr, 11)) # False
# O(n), because there is no match, and every single element has to be checked

"""
In an interview setting, when someone asks about Big O, consider the worst case,
but make sure you make a point of considering best cases as well.
"""


# Space Complexity -------------------------------------------------------------

def create_arr(n):

    new_arr = []

    for num in range(n):
        new_arr.append('new')

    return new_arr

print(create_arr(5))

"""
  The size of the new_arr object scales with the input of N.
  The space complexity is that it will have to take up N items in memory.
"""

def printer(n):

    for x in range(10):
        print("Hello World")

printer(10)
"""
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
"""

# Time complexity: O(n)

# Space complexity: O(1), because it's constant
