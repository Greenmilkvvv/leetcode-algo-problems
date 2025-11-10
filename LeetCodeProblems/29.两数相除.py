#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    # 注意 最大的问题是性能
    # 非常容易超时
    # 一般的代码会在十几个用例之后超时
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1: return INT_MAX

        res = 0
        # 处理边界
        if divisor == INT_MIN: # 如果除数是INT_MIN，那么结果只能是1或者0
            return 1 if dividend == divisor else 0
        
        if dividend == INT_MIN:  # 被除数先减除数
            if divisor == 1: 
                return INT_MIN
            else:
                dividend -= -abs(divisor)
                res += 1

        # 正负号
        sign = 1 if ( (dividend>0) == (divisor>0) ) else -1

        dividend, divisor = abs(dividend), abs(divisor) 
        for i in range(31, -1, -1):
            if (dividend >> i) - divisor >= 0:
                dividend = dividend - (divisor << i)
                # 优化: 这里控制 res >= INT_MAX
                if res > INT_MAX - (1 << i):
                    return INT_MAX
                res += (1 << i)

        return res if sign==1 else -res


            
        
# @lc code=end

