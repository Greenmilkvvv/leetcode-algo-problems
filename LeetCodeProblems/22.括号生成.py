#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start

# 思路: 动态规划

## 当我们知道所有的 i < n 时的情况, 我们可以推断出 i=n 时的所有情况

## 等价地, 我们关注最左边的一个左括号 ( , 它一定有一个与之对应的右括号 ) 我们将这一对括号视作是我们新增近来的括号情况 

## 具体地, i = n 时的所有情况就是: 
### '(' + ( i=p 时的所有括号情况 ) + ')' + ( i=q 时的所有括号情况 ) , 其中 p + q = n - 1 , 0 <= p <= q <= n - 1

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # 初始化存储列表
        res = [[] for _ in range(n+1) ]
        res[0] = ['']

        # 动态规划
        for i in range(1, n+1):
            
            # 遍历 (p,q)
            for p in range(0, i-1 +1):
                q = i-1-p

                # 得出一组 (p,q) 的情况
                res_p_q = [ '(' + x + ')' + y for x in res[p] for y in res[q] ]

                # 将这组情况加入 res[i]
                res[i] += res_p_q

        return res[n]
        
# @lc code=end

