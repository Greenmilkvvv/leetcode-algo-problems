#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start

# 思路: 
## 和前面一样 我们发现 合法的字符串中一定是存在已经闭合的 () 
## 我们把嵌套的括号 看作是不同级别的嵌套括号 比如 () 是一级; ((())) 是三级

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
# @lc code=end

