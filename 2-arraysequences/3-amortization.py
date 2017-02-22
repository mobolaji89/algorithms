# Amortized Analysis of Dynamic Arrays

"""
The strategy of replacing an array with a new, larger array,
might seem slow at first.
As single append operation may require O(n) time to perform.
Our new array allows us to add n new elements before the array must be
replaced again.

Using an algorithmic design pattern called amortization, we can show that
performing a sequence of such append operations on a dynamic array is
actually quite efficient.
"""
