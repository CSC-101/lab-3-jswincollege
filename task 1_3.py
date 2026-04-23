def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value.
#value: 0, 1, 2, 3, 4
#return: False, False, False, True, True


answer = [x for x in range(5) if check(x)]   # What is the value of answer?
#answer = [3, 4]
print()