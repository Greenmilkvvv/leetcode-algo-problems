#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:

        # 发现对于不同量级的数字 有固定的表达方式 只要换一下对应关系即可
        num_to_rome = dict()
        num_to_rome[0] = ('I', 'V', 'X')
        num_to_rome[1] = ('X', 'L', 'C')
        num_to_rome[2] = ('C', 'D', 'M')
        num_to_rome[3] = ('M', '', '')


        num = 0
        for i in range(4): 

            roman1, roman2, roman3 = num_to_rome[i]



            if len(s) >= 4 and s[::-1][0:4][::-1] == roman2 + roman1 * 3:
                num += 8 * 10**i
                s = s[::-1][4:][::-1]



             
            if len(s) >= 3 and s[::-1][0:3][::-1] == roman1 * 3:
                num += 3 * 10**i
                s = s[::-1][3:][::-1]

            elif len(s) >= 3 and s[::-1][0:2][::-1] == roman2 + roman1 * 2:
                num += 7 * 10**i
                s = s[::-1][3:][::-1]


                
            if len(s) >= 2 and s[::-1][0:2][::-1] == roman1 * 2:
                num += 2 * 10**i
                s = s[::-1][2:][::-1]

            elif len(s) >= 2 and s[::-1][0:2][::-1] == roman1 + roman2:
                num += 4 * 10**i
                s = s[::-1][2:][::-1]

            elif len(s) >= 2 and s[::-1][0:2][::-1] == roman2 + roman1:
                num += 6 * 10**i
                s = s[::-1][2:][::-1]

            elif len(s) >= 2 and s[::-1][0:2][::-1] == roman1 + roman3:
                num += 9 * 10**i
                s = s[::-1][2:][::-1]


                    
            if len(s) >= 1 and s[::-1][0:1][::-1] == roman1:
                num += 1 * 10**i
                s = s[::-1][1:][::-1]
            elif len(s) >= 1 and s[::-1][0:1][::-1] == roman2:
                num += 5 * 10**i

        return num

# @lc code=end

