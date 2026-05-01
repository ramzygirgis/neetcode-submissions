# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        next_node = head.next
        previous = None

        while next_node is not None:
            head.next = previous
            previous = head
            head = next_node
            if next_node.next is None:
                next_node.next = previous
                head = next_node
                break
            next_node = next_node.next
        return head