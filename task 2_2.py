def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
    # loop 1: new_list = [4], idx = 0
    # loop 2: new_list = [4, 9], idx = 1
    # loop 3: new_list = [4, 9, 2], idx = 2
    # loop 4: new_list = [4, 9, 2, 1], idx = 3
    #this loop is different because it *appends* the values of the original list to a
    #new list, instead of adding the values themselves
    return new_list                    # How does this loop differ from that above?

result = copy([4, 9, 2, 1])