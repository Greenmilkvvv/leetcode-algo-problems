#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:

    # 思路 
    # 1 从后往前找到第一对 nums[i-1] < nums[i], 
    # 2 在 [i: ] 从后往前中找到第一个大于 nums[i-1] 的数 nums[k] ，交换 i-1 k
    # 3 将 [i: ] 翻转

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 0 特判: 完全降序
        if nums == sorted(nums, reverse=True): 
            nums.sort()
            return None # 什么都不返回

        
        # 1 
        i = len(nums) - 1 
        while (i >= 1) and (nums[i-1] >= nums[i]): 
            i -= 1
        ## 由于已经排除特判 所以最后查到的 i >= 1


        # 2 
        k = len(nums) - 1
        while (k >= i) and (nums[k] <= nums[i-1]): 
            k -= 1  # 必定有 k >= i

        ## 交换
        nums[i-1], nums[k] = nums[k], nums[i-1] 

        
        # 3 反转尾部
        nums[i:] = sorted(nums[i:])

# @lc code=end

