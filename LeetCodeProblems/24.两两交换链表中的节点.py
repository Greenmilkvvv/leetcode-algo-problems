#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def node_to_list(lst: Optional[ListNode]) -> list:

    if lst == None:
        return []

    else: 
        res = []
        while lst.next != None:
            res.append(lst.val)
            lst = lst.next

        res.append(lst.val) # 补上被跳过的最后一个节点
        return res



def list_to_listnode(lst: list) -> Optional[ListNode]:

    if lst == []:
        return None
    
    else:
        lst = lst[::-1]
        lst_res = ListNode(lst[0], None)
        for i in range(1, len(lst)):
            lst_res = ListNode( lst[i] , lst_res )
        return lst_res
    


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        real_lst = node_to_list(head)

        if len(real_lst) < 2:
            res = head
        
        else:
            res_lst = []
            for i in range(0, len(real_lst)-1, 2):  # len(real_lst)-1 是为了防止越界
                res_lst += real_lst[i:i+2][::-1]

            if len(real_lst) % 2 == 1: # 如果长度是奇数，补上最后一个节点
                res_lst.append(real_lst[-1])

            res = list_to_listnode(res_lst)

        return res
  
# @lc code=end

