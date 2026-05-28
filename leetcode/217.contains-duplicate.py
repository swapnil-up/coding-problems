#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_val = set()

        for i in nums:
            if i in set_val:
                return True
            set_val.add(i)
        
        return False
        
# @lc code=end

