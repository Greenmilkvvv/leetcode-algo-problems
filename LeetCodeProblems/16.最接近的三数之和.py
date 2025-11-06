#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:

    # 思路

    ## 先从小到大排序 之后，固定一个数，然后使用双指针，一个指向当前数的下一个数，一个指向最后一个数

    ## 初始化 bias 为当前三个数的和与 target 的差值（绝对值）

    ## 如果当前三个数的和与 target 的差值绝对值小于 bias，则更新 bias

    ## 如果当前三个数的和大于 target，则将右指针左移，反之将左指针右移
    ## 如果当前三个数的和等于 target，则直接返回 结果

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # 排序
        nums.sort()

        # 初始化 偏差
        res = nums[0] + nums[1] + nums[2]
        bias = abs( (nums[0] + nums[1] + nums[2] ) - target )

        # 遍历
        for i in range(len(nums)-2): 
            
            # 左右指针
            L = i+1
            R = len(nums)-1

            # 查询
            while L < R:
                
                # 若发现等于target，直接返回
                if nums[i] + nums[L] + nums[R] == target:
                    res = target
                    bias = 0 
                    break # 也尽量别往后循环了 跳出 while 但没跳出 for
                
                # 若发现更接近的，更新结果
                elif abs(nums[i] + nums[L] + nums[R] - target) < bias:
                    res = nums[i] + nums[L] + nums[R]
                    bias = abs( nums[i] + nums[L] + nums[R] - target )

                # 若当前和大于target，右指针左移
                if nums[i] + nums[L] + nums[R] > target:
                    R -= 1
                # 若当前和小于target，左指针右移
                else:
                    L += 1

        return res
        
# @lc code=end

