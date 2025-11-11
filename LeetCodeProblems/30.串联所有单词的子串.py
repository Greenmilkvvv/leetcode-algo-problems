#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # 1 返回所有可能子串

        ## 这个任务就等价于将 0,...,n-1 按照不重复的顺序全部列出

        ## 使用动态规划的思想
        ## 已知 i <= n-1 的所有可能子串, i = n 时的所有可能子串可以表示为 
        ### 将 s[n] 随机插入由 s[0:n-1] 构成的"每一个"子串中
        ## 
        all_prob_strs = [ [] for _ in range(len(words))]
        all_prob_strs[0] = [ [words[0]] ]

        for i in range(1,len(words)):  
            lst = all_prob_strs[i-1] # 所有的 i 阶子串 组成的列表
            for str_to_connect in lst: # 其中一个 i 阶子串
                # str_to_connect = [ 'xxxx', 'yyyy', 'zzzz', ... ]
                # 将 s[i] 插入这一个子串中 得到字符串组合 new_lst
                new_lst = [ str_to_connect[0:j] + [ words[i] ] + str_to_connect[j:] for j in range(0, len(str_to_connect)+1) ]

                # 将以上可能性加入 all_prob_strs
                all_prob_strs[i] += new_lst

        # 将 all_prob_strs 中的每一个字符串列表组合 转换为字符串
        all_prob_strs = all_prob_strs[-1]
        ## 
        all_prob_strs = [ ''.join(lst) for lst in all_prob_strs ]

        
        # 2 返回所有可能子串在 s 中的位置

        length = len(all_prob_strs[0])
        ans = []
        for k in range( 0, len(s) - length + 1 ):
            if s[ k : k + length ] in all_prob_strs:
                ans.append(k)
                

        return ans
    
# @lc code=end

