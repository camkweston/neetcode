# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None

        if not list1 and not list2:
            return None
        
        elif not list1 and list2:
            return list2
        
        elif list1 and not list2:
            return list1
        
        elif list1.val < list2.val:
            res = list1
            list1 = list1.next
        else:
            res = list2
            list2 = list2.next

        curr = res
        while list1 or list2:
            next_node = None
            if not list1:
                next_node = list2
                list2 = list2.next
            elif not list2:
                next_node = list1
                list1 = list1.next
            elif list1.val < list2.val:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next
        
            curr.next = next_node
            curr = curr.next
        

        return res









        