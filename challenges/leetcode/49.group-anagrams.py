#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for item in strs:
            buckets.setdefault("".join(sorted(list(item))), []).append(item)
        return(list(buckets.values()))


        
# @lc code=end

