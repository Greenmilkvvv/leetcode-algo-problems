#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        medium = 0

        # 合并数组
        merged_nums = nums1 + nums2

        # 排序
        merged_nums.sort()

        # 获取中位数
        if len(merged_nums) % 2 == 0: 
            medium = (merged_nums[len(merged_nums) // 2 - 1] + merged_nums[len(merged_nums) // 2]) / 2

        else: 
            medium = merged_nums[ len(merged_nums) // 2 ]

        return medium
        
# /2 在 Python 3 里永远是 浮点除法，返回 float；列表索引必须是 int，于是 需要 ( len(merged_nums) // 2)

# @lc code=end

