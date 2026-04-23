def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value.
#n's values : 1, 2, 3, 4
#returns: 1, 4, 9, 16

squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above?

# value of squares: [1, 4, 9, 16]
# relation: is just a listing of the return values of square when inputted the given n