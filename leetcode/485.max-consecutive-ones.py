#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i]==0:
                if maxCount<count:
                    maxCount = count
                count = 0
            else:
                count = count + 1
        if maxCount<count:
                maxCount = count
        return maxCount

# @lc code=end
