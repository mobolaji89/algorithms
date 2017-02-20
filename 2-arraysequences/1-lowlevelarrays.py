#Low Level Arrays

"""
Low-level computer architechture:

The primary memory of a computer stored in bits (of information).
Bits are typically grouped into larger units, which are called bytes,
which are 8 bits.
Computers typically use a memory address.
Each byte is associated with a unique address.
    Example: Byte#2144 versus Byte2147.

Arrays:

Computer hardware is designed, in theory, so that any byte of the main memory
can be efficiently accessed.
Computer's main memory performs as a random access memory (RAM).
It's just as easy to retrieve byte #86753367 as it is to retrieve #311
An individual byte of memory can be stored or retrieved in O(1) (constant) time.

Programming languages keep track of the association between an identifier and
the memory address.
A group of related variables can be stored one after another in a contiguous
portion of the computer's memory.
We can denote such representation as an Array.
A text string is stored as an ordered sequence of individual characters.
Python internally represents each Unicode character with 16 bits (i.e., 2 bytes).

Referential Arrays:

A single list instance may include multiple references to the same object as
elements of the list.
A single object can be an element of two or more lists.
When computing the slice of a list, the result is a new list instance.
The new list has references to the same elements that are in the original list.
"""
