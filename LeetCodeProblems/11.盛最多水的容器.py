#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:

    # 在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽 底边宽度 −1​ 变短：

    # 若向内 移动短板 ，水槽的短板 min(h[i],h[j]) 可能变大，因此下个水槽的面积 可能增大 。
    # 若向内 移动长板 ，水槽的短板 min(h[i],h[j])​ 不变或变小，因此下个水槽的面积 一定变小 。

    # 因此，初始化双指针分列水槽左右两端，循环每轮将短板向内移动一格，并更新面积最大值，直到两指针相遇时跳出；即可获得最大面积。

    def maxArea(self, height: List[int]) -> int:


        loc1, loc2 = 0, len(height)-1 # 初始化指针
        max_area = (loc2 - loc1) * min(height[loc1], height[loc2]) # 初始化答案

        while loc1 != loc2: 
            # 短板内移
            if height[loc1] < height[loc2]: 
                loc1 += 1 

            elif height[loc1] >= height[loc2]: 
                loc2 -= 1

            # 比较更新答案
            max_area = max(max_area, (loc2 - loc1) * min(height[loc1], height[loc2]))

        return max_area

# @lc code=end

