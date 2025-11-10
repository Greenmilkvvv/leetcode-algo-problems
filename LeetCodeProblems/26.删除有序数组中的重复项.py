#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    # 思路 
    ## 弄一个字典 存储每个数字出现的次数
    ## 之后使用 .remove(value) 这一个操作
    def removeDuplicates(self, nums: List[int]) -> int:

        val_counts = dict()

        for num in nums:

            if num not in list(val_counts.keys()):
                val_counts[num] = 0

            val_counts[num] += 1
        
        for key, value in val_counts.items():
            if value > 1: 
                for _ in range(value-1): 
                    nums.remove(key) 

        return len(nums)
        
# @lc code=end

