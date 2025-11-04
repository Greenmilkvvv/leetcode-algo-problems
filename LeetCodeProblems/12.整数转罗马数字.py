#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    # 1 <= num <= 3999
    def intToRoman(self, num: int) -> str:

        # 将罗马数字的映射关系存储在字典中
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # 获取各个数字 
        num1 = num
        digits = []
        while num1 != 0: 
            digits.append(num1 % 10)
            num1 = num1//10

        # 将各个数字转化为罗马数字
        expression = [] # 初始化列表 装载罗马字符
        for i, digit in enumerate(digits): 

            if i == 0: 
                if 0 <= digit <= 3:
                    expression.append("I" * digit)
                elif digit == 4:
                    expression.append("I" + "V")
                elif 5 <= digit <= 8: 
                    expression.append("V" + "I" * (digit - 5))
                elif digit == 9:
                    expression.append("IX")

            if i == 1: 
                if 0 <= digit <= 3:
                    expression.append("X" * digit)
                elif digit == 4:
                    expression.append("X" + "L")
                elif 5 <= digit <= 8:
                    expression.append("L" + "X" * (digit - 5))
                elif digit == 9:
                    expression.append("XC")

            if i == 2:
                if 0 <= digit <= 3:
                    expression.append("C" * digit)
                elif digit == 4:
                    expression.append("C" + "D")
                elif 5 <= digit <= 8:
                    expression.append("D" + "C" * (digit - 5))
                elif digit == 9:
                    expression.append("CM")

            if i == 3:
                expression.append("M" * digit)

        # 将列表中的罗马字符拼接成字符串
        ans = "".join(expression[::-1])

        # 或者下面的也可以 效率略差
        # ans = ""
        # for rome in expression[::-1]: 
        #     ans += rome

        return ans

# @lc code=end

