#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through list
        for i in range(len(nums)):
            # get second loop for other number (can't be same as i)
            for j in range(i+1, len(nums),1):
                # check and return locations
                if nums[i]+nums[j] == target:
                    return [i, j]
        return []


        
# @lc code=end
