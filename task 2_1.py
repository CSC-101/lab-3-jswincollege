def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
        # loop 1: total = 4, num = 4
        # loop 2: total = 13, num = 9
        # loop 3: total = 15, num = 2
        # loop 4: total = 16, num = 1
    return total

result = tally([4, 9, 2, 1])
