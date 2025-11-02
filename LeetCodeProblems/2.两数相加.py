#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 当前位数字
        self.next = next    # 下一位节点（或 None）

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 数字 342 在 LeetCode 里会变成这样一个链表：
        ## 2 → 4 → 3 → None
        ## l = ListNode(2, ListNode(4, ListNode(3)))

        # 给出 i 来存储当前 val1 + val2 是否需要进位 ( i=0/1 )
        i = int( l1.val + l2.val >= 10 ) # 0 or 1

        # 创建一个新链表，存储结果
        node1 = ListNode( (l1.val + l2.val)%10 , None ) # 当前位数字
        node = node1


        if l1.next != None and l2.next != None: 
            while l1.next != None and l2.next != None: # 只要有一个链表还有数字，就继续循环
                node.next = ListNode( (l1.next.val + l2.next.val + i) % 10)

                i = int( (l1.next.val + l2.next.val + i) >= 10)
                l1, l2 = l1.next, l2.next

                node = node.next # node 指向下一个节点


        if l1.next != None and l2.next == None: # 如果 l2 没有数字了，l1 还有数字 
            while l1.next != None: 
                node.next = ListNode( (l1.next.val + 0 + i) % 10 )
                i = int( (l1.next.val + 0 + i) >= 10) 
                l1 = l1.next

                node = node.next 


        if l1.next == None and l2.next != None: # 如果 l1 没有数字了，l2 还有数字
            while l2.next != None: 
                node.next = ListNode( (l2.next.val + i) %10  )
                i = int( (l2.next.val + 0 + i) >= 10 )
                l2 = l2.next

                node = node.next

        if i == 1: 
            node.next = ListNode(1) # 如果最后一位相加需要进位，则再添加一个节点
        else: 
            node.next = None
            
        # node1  ─┐
        #         ├─-> [val | next]  <- 这块内存才是真正的结点, 直接返回node1 
        # node  ─┘

        return node1 

# @lc code=end

