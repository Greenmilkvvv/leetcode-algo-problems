#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 链表 -> 列表
        the_next = head.next
        to_list = [head.val]
        while the_next != None: 
            to_list.append(the_next.val)
            the_next = the_next.next

        # 特例
        if len(to_list) == 1:
            res = None

        else:
            # 去除倒数第 n 个结点
            to_list = to_list[0:len(to_list)-n] + to_list[len(to_list)-n+1:]
            
            # 列表 -> 链表
            to_list = to_list[::-1]
            res = ListNode(to_list[0], None)
            for i in range(1,len(to_list)):
                res = ListNode(to_list[i], res)

        return res
# @lc code=end

