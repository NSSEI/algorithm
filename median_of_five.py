def median_of_five(nums):
    if nums[0] > nums[1]:
        win1 = nums[0]
        lose1 = nums[1]
    else:
        win1 = nums[1]
        lose1 = nums[0]
    if nums[2] > nums[3]:
        win2 = nums[2]
        lose2 = nums[3]
    else:
        win2 = nums[3]
        lose2 = nums[2]

    if win1 > win2:
        if nums[4] > lose1:
            return nums[4] if win2 > nums[4] else win2
        else:
            return lose1 if win2 > lose1 else win2
    else:
        if nums[4] > lose2:
            return nums[4] if win1 > nums[4] else win1
        else:
            return lose2 if win1 > lose2 else win1


if __name__ == "__main__":
    print(median_of_five([5, 4, 3, 2, 1]))
    print(median_of_five([3, 2, 1, 4, 5]))