#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # loop from end to start
        for i in range(len(digits) - 1, -1, -1):
            # add one to the number
            digits[i] = (digits[i]+1)%10
            print("digits i", digits[i])
            # check if number is now 0, in which case carry
            if digits[i] == 0:
                # check if this is the foremost element 
                print("i", i)
                if i==0:
                    #insert a digit to start
                    digits.insert(0, 1)
                    break
                # if it isn't add one to the number before
                # digits[i-1] = (digits[i-1]+1)%10 # don't load eagerly
            else:
                break
        return digits
        
# @lc code=end

# States are just the digits themselves and whether a carry exists, and even then the carry is implicit, otherwise the loop would've ended
# Invariant is that after each digit, everything to the right is fixed
# For 9,9 I was modifying a digit eagerly when there was no need