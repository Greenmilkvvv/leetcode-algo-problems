#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans_lst = [] # 初始化组合列表

        # 1 特判
        if nums == None or len(nums) < 3:
            ans_lst = []
        
        # 2 排序 从小到大
        nums.sort()

        # 3 遍历

        for i in range(len(nums)): 
            
            # 如果 nums[i] > 0 则不可能有解
            if nums[i] > 0:
                break # 直接结束循环

            # 如果当前元素在之前已经出现过, 则跳过, 避免重复解
            if (i >= 1) and (nums[i] == nums[i-1]): 
                continue

            # 执行查询
            L = i+1 # 左指针
            R = len(nums)-1 # 右指针

            # 对 i 之后的元素进行配对的查询
            while L < R:

                if nums[i] + nums[L] + nums[R] == 0: # 如果和为0
                    ans_lst.append([nums[i], nums[L], nums[R]])
                    
                    # 接下来移动指针, 并跳过重复的元素
                    while (L < R) and (nums[L] == nums[L+1]):
                        L += 1
                    while (L < R) and (nums[R] == nums[R-1]):
                        R -= 1

                    L, R = L+1, R-1 # 移动指针
                
                elif nums[i] + nums[L] + nums[R] < 0: # 如果和小于0
                    L += 1 # 移动左指针 寻求更大解

                else: # 如果和大于0
                    R -= 1 # 移动右指针 寻求更小解

        return ans_lst
        
# @lc code=end

