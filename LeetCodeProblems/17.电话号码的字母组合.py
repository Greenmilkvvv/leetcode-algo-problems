#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # 确定映射关系
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # 构建嵌套列表 形状根据 digits 确定
        lengths = [ len( mapping[x] ) for x in digits ]

        # 创建多维查询列表 维数对应 lengths 
        res = [ [] for _ in lengths ]

        # 逐层填充
        for i, digit in enumerate(digits):
            res[i] = mapping[digit]

        # 逐层合并
        for i in range(len(res) - 1):
            res[i + 1] = [ x+y for x in res[i] for y in res[i + 1] ]

        return res[-1]
    
# @lc code=end

