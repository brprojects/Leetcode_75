from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# In a linked list of size n, where n is even, the ith node (0-indexed) 
# of the linked list is known as the twin of the (n-1-i)th node.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Solution: Reverse the first half of the linked list using fast and slow pointers to get mid point. Traverse both lists simultaneously finding the max twin sum
def pairSum(head: Optional[ListNode]) -> int:
    reverse_list_head = None
    fast, slow = head, head
    while fast:
        fast = fast.next.next
        next_node = slow.next
        slow.next = reverse_list_head
        reverse_list_head = slow
        slow = next_node
    max_value = float('-inf')
    while reverse_list_head:
        max_value = max(max_value, slow.val + reverse_list_head.val)
        slow = slow.next
        reverse_list_head = reverse_list_head.next
    return max_value

# [1,3,4,7,1,2,6,7]
linked_list = ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 7, next= ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 6, next= ListNode(val= 7, next= None))))))))
print(pairSum(linked_list))