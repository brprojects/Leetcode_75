from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Given the head of a singly linked list, group all the nodes with odd 
# indices together followed by the nodes with even indices, and return the reordered list.
# Solve the problem in O(1) extra space complexity and O(n) time complexity.

# Solution: Create an even and odd linked list by traversing through the linked list, then put them together
def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    odd = head
    even = evenHead = head.next
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = evenHead
    return head

# [1,3,4,7,1,2,6]
linked_list = ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 7, next= ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 6, next= None)))))))
oddEvenList(linked_list)
new_linked_list = []
while linked_list:
    new_linked_list.append(linked_list.val)
    linked_list = linked_list.next
print(new_linked_list)