#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in t:
                t = t.replace(s[i], "", 1)
        return True if t=="" else False
        
if __name__ == "__main__":
    result=Solution().isAnagram("ab", "a")
    print(f"Result: {result}")
# @lc code=end

# Not too bad forgot to think about the edge case where the two strings are differing length (which wouldn't be possible in anagrams tbf)