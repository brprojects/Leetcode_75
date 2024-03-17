from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# You are given the head of a linked list. Delete the middle node, and return the 
# head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# Solution: Have fast and slow pointer, where fast traverses at twice the speed of slow. When fast is at end of the list slow is at the middle, 
# then turn slow.next into slow.next.next, removing the middle node, slow.next, from the linked list
def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = dummy = ListNode(next=head)
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return dummy.next

# [1,3,4,7,1,2,6]
linked_list = ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 7, next= ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 6, next= None)))))))
deleteMiddle(linked_list)
new_linked_list = []
while linked_list:
    new_linked_list.append(linked_list.val)
    linked_list = linked_list.next
print(new_linked_list)