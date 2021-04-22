def insertion_sort(nums_list):
    for index in range(1, len(nums_list)):
        curr_val = nums_list[index]
        curr_pos = index
        while curr_pos > 0 and curr_val <= nums_list[curr_pos - 1]:
            nums_list[curr_pos] = nums_list[curr_pos - 1]
            curr_pos -= 1
        nums_list[curr_pos] = curr_val
    return nums_list


def quick_sort(nums_list, first, last):
    if first < last:
        split_point = partition(nums_list, first, last)
        quick_sort(nums_list, first, split_point - 1)
        quick_sort(nums_list, split_point + 1, last)
    return nums_list

def partition(nums_list, first, last):
    pivot = nums_list[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and nums_list[left] <= pivot:
            left += 1
        while left <= right and pivot <= nums_list[right]:
            right -= 1
        if right < left:
            done = True
        else:
            nums_list[left], nums_list[right] = nums_list[right], nums_list[left]
    nums_list[first], nums_list[right] = nums_list[right], nums_list[first]
    return right


if __name__ == "__main__":
    print(insertion_sort([9, 9, 10, 11, 5, 4, 3, 2, 1, 7, 8]))
    print(quick_sort([9, 9, 10, 11, 5, 4, 3, 2, 1, 7, 8], 0, 10))