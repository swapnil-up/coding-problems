#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list = [nums[0]]
        # Loop through elements
        for i in range(len(nums)-1):
            print("i", nums[i], nums[i+1])
            print(list)
            # or add into fresh deduplicated list
            if nums[i] != nums[i+1]:
                list.append(nums[i+1])
                nums[len(list)-1]=nums[i+1]
            # if duplicate skip
            else:
                continue
        return len(list)
    
    def removeDuplicates2(self, nums: List[int]) -> int:
        read = 0
        write = 0
        while(read<len(nums)-1):
            if nums[write]!=nums[read]:
                nums[write]=nums[read]
                write = write+1
            read=read+1
        return write+1
    
# @lc code=end

# Took way too long to realize that I can use the deduplicated list's end point as the index where I overwrite the value to the correct one. Now I could even just use an integer pointer instead of a whole list. 

def test_removeDuplicates2():
    test_cases = [
        # (input array, expected new length, expected modified array prefix)
        ([1,1,2], 2, [1,2]),
        ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
        ([1,2,3,4,5], 5, [1,2,3,4,5]),          # no duplicates
        ([1,1,1,1,1], 1, [1]),                  # all duplicates
        ([1], 1, [1]),                           # single element
        ([], 0, []),                             # empty array
        ([1,1,2,2,2,3,4,4,5,5,5,5,6], 6, [1,2,3,4,5,6])  # longer mixed
    ]

    for i, (nums, expected_len, expected_nums) in enumerate(test_cases):
        s = Solution()
        length = s.removeDuplicates2(nums)
        print(f"Test case {i+1}:")
        print(f"Input array: {nums}")
        print(f"Expected length: {expected_len}, Output length: {length}")
        print(f"Expected prefix: {expected_nums}, Array prefix: {nums[:length]}")
        print("-"*40)

if __name__ == "__main__":
    test_removeDuplicates2()