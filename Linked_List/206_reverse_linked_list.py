from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Solution: Traverse the linked list and each node store its next node, attach the current node to the front of the reversed list, 
# update the new front of the reversed list to the current node, then make the stored next node the new current node
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    new_list = None
    current = head
    while current:
        next_node = current.next
        current.next = new_list
        new_list = current
        current = next_node
    return new_list

# [1,3,4,7,1,2,6]
linked_list = ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 7, next= ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 6, next= None)))))))

linked_list = reverseList(linked_list)
new_linked_list = []
while linked_list:
    new_linked_list.append(linked_list.val)
    linked_list = linked_list.next
print(new_linked_list)