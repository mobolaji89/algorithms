# Find the Missing Element

"""
Problem:

Consider an array of non-negative integers. A second array is formed by
shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is
removed to construct the second array.

Input:

    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

    5 is the missing number
"""

"""
If we don’t want to deal with the special case of duplicate numbers,
we can sort both arrays and iterate over them simultaneously.
Once two iterators have different values we can stop.
The value of the first iterator is the missing element.
This solution is also O(NlogN). Here is the solution for this approach:
"""

def finder(arr1,arr2):

    # Sort the arrays
    arr1.sort()
    arr2.sort()

    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1,arr2):
        if num1!= num2:
            return num1

    # Otherwise return last element
    return arr1[-1]

"""
We can use a dictionary(hash) and store the number of times each element appears in
the second array.
Then for each element in the first array we decrement its counter.
Once hit an element with zero count that’s the missing element.
Here is this solution:
"""

import collections

def finder2(arr1, arr2):

    # Using default dict to avoid key errors
    d=collections.defaultdict(int)

    # Add a count for every instance in Array 1
    for num in arr2:
        d[num]+=1

    # Check if num not in dictionary
    for num in arr1:
        if d[num]==0:
            return num

        # Otherwise, subtract a count
        else: d[num]-=1

"""
But what about linear time solution?

By performing a very clever trick, we can achieve linear time and constant
space complexity without any problems.
Here it is: initialize a variable to 0, then XOR every element in the first
and second arrays with that variable.
In the end, the value of the variable is the result, missing element in array2.
"""

def finder3(arr1, arr2):
    result=0

    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2:
        result^=num
        print result

    return result
