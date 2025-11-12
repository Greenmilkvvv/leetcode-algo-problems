#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # # 1 返回所有可能子串

        # ## 这个任务就等价于将 0,...,n-1 按照不重复的顺序全部列出

        # ## 使用动态规划的思想
        # ## 已知 i <= n-1 的所有可能子串, i = n 时的所有可能子串可以表示为 
        # ### 将 s[n] 随机插入由 s[0:n-1] 构成的"每一个"子串中
        # ## 
        # all_prob_strs = [ [] for _ in range(len(words))]
        # all_prob_strs[0] = [ [words[0]] ]

        # for i in range(1,len(words)):  
        #     lst = all_prob_strs[i-1] # 所有的 i 阶子串 组成的列表
        #     for str_to_connect in lst: # 其中一个 i 阶子串
        #         # str_to_connect = [ 'xxxx', 'yyyy', 'zzzz', ... ]
        #         # 将 s[i] 插入这一个子串中 得到字符串组合 new_lst
        #         new_lst = [ str_to_connect[0:j] + [ words[i] ] + str_to_connect[j:] for j in range(0, len(str_to_connect)+1) ]

        #         # 将以上可能性加入 all_prob_strs
        #         all_prob_strs[i] += new_lst

        # # 将 all_prob_strs 中的每一个字符串列表组合 转换为字符串
        # all_prob_strs = all_prob_strs[-1]
        # ## 
        # all_prob_strs = [ ''.join(lst) for lst in all_prob_strs ]

        
        # # 2 返回所有可能子串在 s 中的位置

        # length = len(all_prob_strs[0])
        # ans = []
        # for k in range( 0, len(s) - length + 1 ):
        #     if s[ k : k + length ] in all_prob_strs:
        #         ans.append(k)
                
        # return ans
    
# ============= 以上绝对正确 但是超时了 ============= 

# 下面使用滑动窗口法

        from collections import Counter

        # 特判
        if not s or not words: return []

        # 统计单词长度 (每个单词都等长度)
        one_word = len(words[0])
        word_num = len(words) 
        n = len(s)

        if n < one_word: return []

        words = Counter(words)
        res = []
        for i in range(one_word): 
            cur_cnt = 0 
            left, right = i, i
            cur_Counter = Counter()
            while right + one_word <= n: # right + one_word 是下一个单词的起始位置
                w = s[right: right + one_word] 
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left: left + one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:
                    res.append(left)
        return res

# @lc code=end

