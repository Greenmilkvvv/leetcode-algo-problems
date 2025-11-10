#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        remove_counts = sum([ val == k for k in nums])

        for _ in range( remove_counts ): 
            nums.remove(val)

        return len(nums)
# @lc code=end

