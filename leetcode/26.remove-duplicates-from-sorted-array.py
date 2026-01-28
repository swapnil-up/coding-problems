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
    
# @lc code=end

# Took way too long to realize that I can use the deduplicated list's end point as the index where I overwrite the value to the correct one. Now I could even just use an integer pointer instead of a whole list. 
