#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        real_lists = [ node_to_list(lst) for lst in lists ]

        res = []
        for real_list in real_lists: 
            res += real_list

        res.sort()

        return list_to_listnode(res)
        
# @lc code=end

