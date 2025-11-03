#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start

class Solution:

# 不将 int 转为 str
## 首先 回文的 x 不可能是一个负数 ( x >= 0 )
## 其次 个位不能为 0 ( x % 10**k != 0 for k = 1,2 )
## 再次 要如何对这样一个非负数进行判断? (不用 str )
#            | 
#            |
#           \|/
###  1. 判断最高位数
###  2. 判断最高位和最低位是否相等

    def isPalindrome(self, x: int) -> bool:

        # ========== 字符串法 =============
        # return str(x)[::-1] == str(x)
        # ================================

        # ========== 数值法 =============
        # 个位正整数
        if 0 <= x < 10: 
            ans = True
        # 负数 或者 个位为 0 的大于0数
        elif (x<0) or (x%10==0):
            ans = False
        # 大于 10 的非负整数
        else: 
            # 判断最高位
            order = 1
            while x // 10**order >= 10 : 
                order += 1

            # 判断最高位和最低位是否相等
            y=0
            z=x
            for i in range(0,order+1):
                num = z // 10**(order-i)
                y += num * 10**i
                z -= num * 10**(order-i)

            ans = True if y == x else False

        return ans
  
# @lc code=end

