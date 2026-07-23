#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        state = 0
        length = float('inf')

        for right in range(len(nums)):
            state += nums[right]
            while state>= target:
                length = min(length, right-left+1)
                state -= nums[left]
                left +=1
        if length==float('inf'):
            return 0
        else:
            return length
        
# @lc code=end

if __name__ == "__main__":
    nums = [1,1,1,1,1,1,1,1]
    target = 11
    sol = Solution()
    result = sol.minSubArrayLen(target, nums)
    print(result)