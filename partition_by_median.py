def partition(nums):
    # set nums to [win1, lose1, win2, lose2, ?]
    if nums[0] < nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    if nums[2] < nums[3]:
        nums[2], nums[3] = nums[3], nums[2]

    # move tmp_largest num to nums[4]
    # set nums to [win1, lose1, win2, lose2, tmp_largest]
    if nums[0] < nums[2]:
        nums[2], nums[4] = nums[4], nums[2]
        if nums[2] < nums[3]:
            nums[2], nums[3] = nums[3], nums[2]
    else:
        nums[0], nums[4] = nums[4], nums[0]
        if nums[0] < nums[1]:
            nums[0], nums[1] = nums[1], nums[0]


    # compare win1, win2 to get the median
    # change nums to [lose, lose, median, second_tmp_largest, tmp_largest]
    if nums[0] < nums[2]:
        nums[0], nums[2], nums[3] = nums[3], nums[0], nums[2]
    else:
        nums[0], nums[3] = nums[3], nums[0]

    return nums

if __name__ == "__main__":
    print(partition([5, 4, 3, 2, 1]))
    print(partition([3, 2, 1, 4, 5]))