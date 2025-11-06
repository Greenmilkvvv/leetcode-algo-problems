#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:

        # 思路
        ## 将列表中最短的string作为基准
        ## 初始化一个空字符串 每次添加最短string中的字符并进行查询

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # 1 找到 shortest string
        shortest = min(strs, key=len)

        # 2 正向 初始化一个空字符串
        common = ''

        # 3 正向 查询所有string中是否都存在该字符
        for letter in shortest: 
            common += letter

            # 如果符合 则进行下一轮
            if all( (string[:len(common)] ==common) for string in strs):
                continue

            # 如果不符合 则删除最后一个字符 并跳出循环
            else:
                common = common[:-1]
                break

        return common
       
# @lc code=end

