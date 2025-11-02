#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    # 思路
    ## 将字符串按照索引分割，然后按照顺序拼接
    ### 具体地 先将字符串 s 按照长度切片为 numRows, numRows-2, numRows, numRows-2,..., 循环往复 直到切片结束
    ### 再将所有长度 numRows-2 的小切片颠倒顺序 头尾用 "" 补足
    ###
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1: 
            return s
        
        if numRows > 1: 
            # 填充
            lst_str = list(s)
            len_col = 2*numRows-2
            num_filled = len_col - ( len(s) % len_col )
            for i in range(num_filled):
                lst_str.append("")

            # 分割为长度为 2*numRows -2 的切片
            # 重新排序
            lst_split = []
            for i in range( 0 , len(s) , len_col ): 
                lst = lst_str[i:i+len_col]
                # lst = [lst[:numRows], ['']+lst[numRows:][::-1]+['']]
                lst_split.append( lst[:numRows] )
                lst_split.append( ['']+lst[numRows:][::-1]+[''] )

            ans = ''
            for i in range( numRows ):
                for j in range( len(lst_split) ): 
                    ans += lst_split[j][i]

            return ans
        
# @lc code=end


