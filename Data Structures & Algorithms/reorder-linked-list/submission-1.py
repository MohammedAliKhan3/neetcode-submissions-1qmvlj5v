# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow,fast = head,head.next

        # finding the mid of linked List.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        
        # Reversing the 2nd Half of Linked List.
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp


        # arraing the linked list.
        first , second = head, prev
        while second:
            tmp1, tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first , second = tmp1 , tmp2













