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

        # 先查出 digits 能够产出多少组合
        lengths = [len( mapping[num] ) for num in digits]

        # 确定组合的长度
        res_length = 1
        for i in range(len(lengths)):
            res_length *= lengths[i]

        # 据此可初始化答案列表
        res = [''] * res_length

        # 第一个字符将会平均分配给后面的组合 而其长度都等于 res_length // lengths[0]
        # 据此构建一个循环 先后分配

        for i, digit in enumerate(digits):  # 对于每一个字符 查询其需要重复分配多少次
            repeat = res_length // lengths[i]
            for j in range(repeat):  # 对于每一个重复次数
                

            
        
        
# @lc code=end

