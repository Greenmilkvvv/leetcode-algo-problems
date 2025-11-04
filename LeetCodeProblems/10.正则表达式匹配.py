#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:

# =========================================
# 我的思路： (已经放弃)

# 显然, "*" 可以进行复制或消除, 而且不会重叠出现, 所以, 可以把字符串按照 "*" 使用 .split("*") 成多个子串

# 对于每一个子串, 
# - 首先观察, 最后一个字符是否为 "." , 如果是, 则可以匹配任意字符, 并进行任意次扩展
# - 如果最后一个字符不是 "." , 而是具体的字符, 则把其进行扩展考虑

# 那么一共能够扩展多少次呢? 事实上是有限的, 因为 len(s) >= len(p) 是肯定的, 所以, 对于每一个子串, 最多可以进行 k = len(s) - ( len(p) - num(*) ) 次扩展

# =========================================
# 思路 (动态规划): 来自 kimi 老师 

# 把 DP 想成“填表格”：

# 行号 i 表示 s 前 i 个字符，列号 j 表示 p 前 j 个字符，格子 dp[i][j] 只存一句话——
# “s[:i] 能不能被 p[:j] 匹配？”

# 我们从空串开始，一行一行把表格填满，最后看右下角那个格子即可。

# =========================================

    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p) 

        # 初始化 dp 表 dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配 (True / False)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True # 空列表必定匹配
        # dp[0][1] = False # 空列表与 p[0] 必定不可能匹配 无论是 * . 还是其他具体字符


        # 首先, 当 s 为空列表时, 先填满 dp 表的第一列 dp[0][j] 即 '' 和 p[:j-1+1] 的匹配 (j = 0, 1, ..., n)
        for j in range(2 , n+1): 

            # 当 dp[0][j-2] = True , p[j-1] 必定只能为 * , 才能让 dp[0][j] = True
            # 当 dp[0][j-2] = False, p[j-2] 和 p[j-1] 不管是啥都没救了

            dp[0][j] = True if ( dp[0][j-2] == True and p[j-1] == '*' ) else False

        # 之后 注意到 只要 p 是空字符串 除了 dp[0][0]=True 其他都不可能匹配 都为False

        # 再之后 进行填表, 从 dp[1][1] 开始, 一直到 dp[m][n]
        # 有那么几种情况 

        for i in range(1, m+1): 
            for j in range(1, n+1): 

                if p[j-1] == "*": 

                    # 0次, 看 dp[i][j-2]==True
                    # >=1次，必定要求 s[i-1] 与 p[j-2] 相匹配, 且 dp[i-1][j] == True

                    dp[i][j] = dp[i][j-2] or ( 
                       dp[i-1][j] if ( p[j-2] == '.' or s[i-1] == p[j-2] ) else False 
                    )                   
                
                else: 
                    dp[i][j] = dp[i-1][j-1] if (p[j-1] == '.' or s[i-1] == p[j-1]) else False

        return dp[m][n]

# @lc code=end

