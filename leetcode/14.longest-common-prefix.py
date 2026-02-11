#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
import sys
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        position = 0
        shortest_element = min(strs, key=len)
        if(len(strs)==1):
            return strs[0]
        for i in range(len(shortest_element)):
            for j in range(len(strs)-1):
                print(shortest_element, i, j)
                if(strs[j][i]!=strs[j+1][i]):
                    position = i
                    return shortest_element[:position]
        return shortest_element[:len(shortest_element)]
    
        
# @lc code=end

if __name__ == "__main__":
    if len(sys.argv)>1:
        input = sys.argv[1:]
        sol = Solution()
        result = sol.longestCommonPrefix(input)
        print(f"Input: {input}")
        print(f"Output: {result}")


# Stumbled on way too many edge cases tbh. Didn't realize that if list's smallest is the prefix itself then I just need the length instead of a specific position. Bruteforced my way through this.