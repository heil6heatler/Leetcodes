# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        nodemap={}
        while temp is not None:
            if temp in nodemap:
                return True
            else:
                nodemap[temp]=1

            temp=temp.next
        return False