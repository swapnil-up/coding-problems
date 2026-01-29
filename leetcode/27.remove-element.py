#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k=k+1
        return k
        
# @lc code=end

#Similar to 26, though I still took a while. Not fluid. Got confused about how to add stuff in and how I need to fix array in place. Did do list first, then used integer k instead of a list. Wasn't that hard to change the implementation once you realize that the list is used only to get the last index which is where the overwrite would happen in the original line, which is what k does too, but with less guard rails so it looks flimsy. That's why it's called the write pointer. Oh. Because everything before that pointer is in correct state in every iteration of the loop. While the for loop is the read that just iterates everytime. 
