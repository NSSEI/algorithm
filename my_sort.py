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

def heap_sort(nums):
    n = len(nums)
    for i in reversed(range(n//2)):
        heapify(nums, i, n)
    for i in reversed(range(n)):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i)
    return nums

def heapify(nums, index, heap_size):
    change = index
    n = heap_size
    leftchild = (index << 1) + 1
    rightchild = leftchild + 1
    if leftchild < n and nums[change] < nums[leftchild]:
        change = leftchild
    if rightchild < n and nums[change] < nums[rightchild]:
        change = rightchild
    if change != index:
        nums[change], nums[index] = nums[index], nums[change]
        heapify(nums, change, n)




if __name__ == "__main__":
    print(insertion_sort([9, 9, 10, 11, 5, 4, 3, 2, 1, 7, 8]))
    print(quick_sort([9, 9, 10, 11, 5, 4, 3, 2, 1, 7, 8], 0, 10))
    print(heap_sort([9, 9, 10, 11, 5, 4, 3, 2, 1, 7, 8]))