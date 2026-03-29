# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        linked_list_reverse = []
        dummy = head
        while dummy:
            linked_list_reverse.append(dummy.val)
            dummy = dummy.next

        linked_list_reverse.reverse()

        if linked_list_reverse == []:
            return None

        dummyList = ListNode(linked_list_reverse[0])
        p1 = dummyList

        for i in range(1,len(linked_list_reverse)):
            dummyList.next = ListNode(linked_list_reverse[i])
            dummyList = dummyList.next

        return p1
