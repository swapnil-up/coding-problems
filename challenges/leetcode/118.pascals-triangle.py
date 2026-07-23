#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc=[[1]]
        for i in range(1,numRows):
            line=[]
            prev_line=pasc[i-1]
            for j in range(i+1):
                if j==0 or j==i:
                     line.append(1)
                else:
                    value = prev_line[j-1] + prev_line[j]
                    line.append(value)
            if len(line)>0:
                pasc.append(line)
            # print(pasc)                
        return pasc
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(8))
# @lc code=end

# Fucking loops man, took me way too long and worked very brittle, my understanding needs help.