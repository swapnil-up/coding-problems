#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
import sys


class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        i = 0
        while i < len(s):
            # print(i, integer, s[i])
            if s[i] == "M":
                integer +=1000
                i=i+1
            elif s[i] == "D":
                integer +=500
                i=i+1
            elif s[i] == "C":
                if i<len(s) - 1 and s[i+1]=="D":
                    integer +=400
                    i=i+2
                elif i<len(s) - 1 and s[i+1]=="M":
                    integer +=900
                    i=i+2
                else:
                    integer +=100
                    i=i+1
            elif s[i] == "L":
                integer +=50
                i=i+1
            elif s[i] == "X":
                if i<len(s) - 1 and s[i+1]=="L":
                    integer +=40
                    i=i+2
                elif i<len(s) - 1 and s[i+1]=="C":
                    integer +=90
                    i=i+2
                else:
                    integer +=10
                    i=i+1
            elif s[i] == "V":
                integer +=5
                i=i+1
            elif s[i] == "I":
                if i<len(s) - 1 and s[i+1]=="V":
                    integer +=4
                    i=i+2
                elif i<len(s) - 1 and s[i+1]=="X":
                    integer +=9
                    i=i+2
                else:
                    integer +=1
                    i=i+1
        return integer
        
# @lc code=end

if __name__ == "__main__":
    if len(sys.argv)>1:
        input = sys.argv[1]
        sol = Solution()
        result = sol.romanToInt(input)
        print(f"Input: {input}")
        print(f"Output: {result}")


# I like the cli input that I added in, but I don't like how I mapped each case. We're not making the most optimal solution atm, but even just peeking at techniques I can see using dictionary and just looking ahead to see if we need to subtract to condense to one rule.