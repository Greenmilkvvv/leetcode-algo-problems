#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        # 去空格
        s = s.strip() 

        # 符号判断
        if len(s) == 0:
            sign = 1
            s = '0'
        elif s[0] == '-': 
            sign = -1
            s = s[1:]
        elif s[0] == '+': # 一定是elif而不是else
            sign = 1
            s = s[1:]
        else: 
            sign = 1
        # ===========================
        # 一定要注意 第二个判断如果使用 if 而不是 elif , 那么第三个判断 else 一定会被算在第二个 if 里面, else 判断中的这个 sign=1 会覆盖第一个 if 的 sign=-1 从而出错!!!!!!
        # ===========================

        # 切出第一个非数字字符
        s1 = ''
        for i in range(len(s)): 
            if s[i].isdigit():
                s1 += s[i]
            else: 
                break

        # 跳出字符串的前置0
        s1 = '0' if len(s1) == 0 else s1
        while s1[0] == '0' and len(s1) > 1: 
            s1 = s1[1:]

        s1 = int(s1)
        # 转换数字
        # num = sign * int(s)

        # 舍入
        if sign * s1 > 2**31 - 1:
            return 2**31 - 1
        elif sign * s1 < -2**31:
            return -2**31
        else:
            return sign * s1
 
# @lc code=end

