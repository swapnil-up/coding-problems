#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        state=0
        avg=[]
        for right in range(len(nums)):
            state+=nums[right]
            if right>= k-1:
                avg.append(state/k)
                state-=nums[left]
                left+=1
        return max(avg)
    
if __name__ == "__main__":
    nums = [5]
    k = 1

    sol = Solution()
    result = sol.findMaxAverage(nums, k)

    print("Result:", result)

        
# @lc code=end

# Now that I've got 10 solved, I think I'd like to get better than brute force solution. I looked up the logic and applied it here. Four things to remember in each iterations state: left, right, state (content of window) and ans (logic needed for the question). Constraint is the length of the window. Invariant is the state of the current window.