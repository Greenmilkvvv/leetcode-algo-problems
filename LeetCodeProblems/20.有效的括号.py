#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:

    # 思路
    ## 如果是合法使用的括号 那么在字符串的中心一定存在一个 ()/[]/{} 一经发现 我们立刻将之删除
    ## 使用 while 重复刚才的动作
    ## 如果最后字符串为空 那么说明是有效的括号

    def isValid(self, s: str) -> bool:

        judge = ( '()' in s ) or ( '[]' in s ) or ( '{}' in s )

        while judge: # 只要存在合法的括号 就一直循环
            for i in range( len(s) ): # 遍历字符串
                if s[i:i+2] in ['()', '[]', '{}']: # 判断当前字符是否是合法的括号

                    s = s[:i] + s[i+2:] # 切除第一个闭合括号

                    judge = ( '()' in s ) or ( '[]' in s ) or ( '{}' in s )

                    break # 达成目的 跳出 for 循环

        res = True if ( s=='' ) else False
        
        return res
# @lc code=end