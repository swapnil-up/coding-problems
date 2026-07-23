#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=list(s)
        t1=list(t)
        if len(s1) != len(t1):
            return False
        for i in s1:
            if i not in t1:
                return False
            t1.remove(i)
        return True
        
if __name__ == "__main__":
    result=Solution().isAnagram("ab", "a")
    print(f"Result: {result}")
# @lc code=end

# Not too bad forgot to think about the edge case where the two strings are differing length (which wouldn't be possible in anagrams tbf)