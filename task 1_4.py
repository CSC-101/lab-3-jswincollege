def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value.
#value: 3, 4
#return: 4, 5

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value.
#value: 0, 1, 2, 3, 4
#return: False, False, False, True, True


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer?
print()

#value: [4,5]
