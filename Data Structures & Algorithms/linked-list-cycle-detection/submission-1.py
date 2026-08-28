# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        currNode = head
        nextNode = head

        while nextNode and nextNode.next:
            

            currNode = currNode.next
            nextNode = nextNode.next.next
            if currNode == nextNode:
                return True
        return False