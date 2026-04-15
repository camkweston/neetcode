# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_depth = 0
        max_depth = 1000

        curr = head

        while curr:
            curr_depth +=1
            curr = curr.next

            if curr_depth > max_depth:
                return True
        
        return False




        