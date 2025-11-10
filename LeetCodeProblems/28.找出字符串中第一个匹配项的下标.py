#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        k = len(needle)

        res = -1
        for i in range(0, n-k+1): # 使用 n-k+1 而不是 n-k，是为了避免 out of range
            if haystack[i:i+k] == needle:
                res = i
                break

        return res
        
# @lc code=end

