#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list1, list2 = node_to_list(list1), node_to_list(list2)

        list_res = list1 + list2
        list_res.sort()

        list_res = list_to_listnode( list_res )

        return list_res
        
# @lc code=end

