#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    """
    分析:

    首先是“匹配成功”，这个用栈来实现。为了给第2步做准备，我们要在匹配成功时做个记号，这里开辟一个数组，匹配成功时，在'('和")'的索引位置处记为1。

    然后统计数组里面连续1的个数，最长的那个就是结果

    ---

    作者：苏灿

    链接：https://leetcode.cn/problems/longest-valid-parentheses/solutions/2719468/chao-jian-dan-fang-fa-zhi-hui-gua-hao-pi-nbby/
    """
    def longestValidParentheses(self, s: str) -> int:
        stack = [] # 存储左括号索引
        maxL = 0 # 最长有效括号长度
        n=len(s)
        tmp = [0 for _ in range(n)] # 存储数组
        cur = 0 # 当前连续1的个数

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                tmp[i] = 1
                tmp[stack.pop()] = 1 # 匹配成功，记录1
                

        # 最长的 1 
        for i in range(n):
            if tmp[i] == 1: 
                cur += 1
            else: 
                maxL = max(maxL, cur)
                cur = 0

        return max(maxL, cur)
# @lc code=end

