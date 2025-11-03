#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:

        if x == 0: 
            ans = 0
        elif x > 0: 
            ans = int(str(x)[::-1])
        elif x < 0: 
            ans = (-1) * int(str(-x)[::-1])

        return ( ans if (-2**31 <= ans and ans <= 2**31-1) else 0 )
        
# @lc code=end

