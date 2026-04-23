def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
        # loop 1: new_list = [5], value = 4
        # loop 2: new_list = [5, 10], value = 9
        # loop 3: new_list = [5, 10, 3], value = 2
        # loop 4: new_list = [5, 10, 3, 2], value = 1
    return new_list

result = increment_all([4, 9, 2, 1])