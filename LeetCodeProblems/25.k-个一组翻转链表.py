#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        real_lst = node_to_list(head)
        res_lst = []


        if len(real_lst) < k: # 如果链表长度小于k，则不翻转
            res = head

        else:
            for i in range(0, len(real_lst)-k+1, k): 
                # 使用 len(real_lst) - k + 1 是为了避免将最后一个不足k的子链表翻转 (事实是为了不触发 out of range(index) )
                res_lst += real_lst[i:i+k][::-1] # 翻转子链表

            rest_to_add = len(real_lst) % k
            if rest_to_add != 0: # 如果最后一个子链表不足k个节点，则不翻转
                res_lst += real_lst[-rest_to_add: ]

            res = list_to_listnode(res_lst)

        return res
        
# @lc code=end

