def insertion_sort(nums_list):
    for index in range(1, len(nums_list)):
        curr_val = nums_list[index]
        curr_pos = index
        while curr_pos > 0 and curr_val <= nums_list[curr_pos - 1]:
            nums_list[curr_pos] = nums_list[curr_pos - 1]
            curr_pos -= 1
        nums_list[curr_pos] = curr_val
    return nums_list



if __name__ == "__main__":
    print(insertion_sort([9,9,10,11,5,4,3,2,1,7,8]))