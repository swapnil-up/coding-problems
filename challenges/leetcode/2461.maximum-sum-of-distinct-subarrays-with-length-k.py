#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
from typing import List


class Solution:
    # def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    #     left = 0
    #     state = 0
    #     sum=0
    #     sub=[]
    #     for right in range(len(nums)):
    #         state += nums[right]
    #         sub.append(nums[right])
    #         # print(state, sub)
    #         if right >= k-1:
    #             if state>sum and len(sub) == len(set(sub)):
    #                 sum=state
    #             state -= nums[left]
    #             sub.pop(0)
    #             left += 1
    #     return sum
    

    def findMaxSumSubArray(self, nums: List[int], k: int) -> int:
        left = 0
        state = 0
        sum=0
        for right in range(len(nums)):
            state += nums[right]
            if right >= k-1:
                if state>sum:
                    sum=state
                state -= nums[left]
                left += 1
        return sum
        
# @lc code=end

if __name__ == "__main__":
    nums= [1,5,4,2,9,9,9]
    k = 3
    sol = Solution()
    result = sol.findMaxSumSubArray(nums, k)
    print(result)
