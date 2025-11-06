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



            if len(s) >= 4 and s[-4:] == roman2 + roman1 * 3:
                num += 8 * 10**i
                s = s[:-4]
                continue



            if len(s) >= 3 and s[-3:] == roman1 * 3:
                num += 3 * 10**i
                s = s[:-3]
                continue

            elif len(s) >= 3 and s[-3:] == roman2 + roman1 * 2:
                num += 7 * 10**i
                s = s[:-3]
                continue


                
            if len(s) >= 2 and s[-2:] == roman1 * 2:
                num += 2 * 10**i
                s = s[:-2]
                continue

            elif len(s) >= 2 and s[-2:] == roman1 + roman2:
                num += 4 * 10**i
                s = s[:-2]
                continue

            elif len(s) >= 2 and s[-2:] == roman2 + roman1:
                num += 6 * 10**i
                s = s[:-2]
                continue

            elif len(s) >= 2 and s[-2:] == roman1 + roman3:
                num += 9 * 10**i
                s = s[:-2]
                continue


                    
            if len(s) >= 1 and s[-1:] == roman1:
                num += 1 * 10**i
                s = s[:-1]
                continue

            elif len(s) >= 1 and s[-1:] == roman2:
                num += 5 * 10**i
                s = s[:-1]
                continue

        return num

# @lc code=end

