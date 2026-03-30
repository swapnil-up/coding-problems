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

    # assumes sorted array
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        while start<end:
            sum = nums[start]+nums[end]
            if sum == target:
                return [start, end]
            if sum<target:
                start=start+1
            else:
                end=end-1
        return []


        
# @lc code=end

if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 9),
        ([5, 75, 25], 100),
        ([1, 5, 3, 7], 8),
        ([10, -2, 4, 7], 5),
        ([0, 4, 3, 0], 0),
        ([-1, -2, -3, -4, -5], -8),
        ([1, 2], 3),
        ([1, 2], 4),
    ]

    for nums, target in test_cases:
        r1 = s.twoSum(nums, target)
        r2 = s.twoSum2(nums, target)

        print(f"nums={nums}, target={target}")
        print(f"twoSum  -> {r1}")
        print(f"twoSum2 -> {r2}")
        print("-" * 30)