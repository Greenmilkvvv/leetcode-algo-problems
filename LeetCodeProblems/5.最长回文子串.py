#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:

# 中心扩展

## 可以从每一种边界情况开始「扩展」，也可以得出所有的状态对应的答案。

## 边界情况即为子串长度为 1 或 2 的情况。我们枚举每一种边界情况，并从对应的子串开始不断地向两边扩展。如果两边的字母相同，我们就可以继续扩展，例如从 P(i+1,j−1) 扩展到 P(i,j)；如果两边的字母不同，我们就可以停止扩展，因为在这之后的子串都不能是回文串了。

    # 从某两个索引开始扩展，直到不能再扩展为止
    def ExpandFromCentre(self, s: str, left: int, right: int) :
        while (left>=0) and (right<len(s)) and (s[left] == s[right]): 
            left = left - 1 
            right = right + 1

        return s[left+1 : right-1+1] # 注意切片的边界

    def longestPalindrome(self, s: str) -> str:

        ans = '' # 初始化答案

        for i in range(0, len(s)-1): 
            str1 = self.ExpandFromCentre(s, i, i+1) # 奇数长度的字符串
            
            str2 = self.ExpandFromCentre(s,i,i+2) # 偶数长度的字符串
            
            str_target = str1 if len(str1) > len(str2) else str2

            ans = str_target if len(ans) < len(str_target) else ans
        
        ans = ans if len(ans) > 1 else s[-1]
            
        return ans
    
# @lc code=end

