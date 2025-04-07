# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        reversedLinkedArr = []
        while(head is not None):
            reversedLinkedArr.append(head.val)
            head = head.next
        linkedArr = reversedLinkedArr[:]
        reversedLinkedArr.reverse()
        if reversedLinkedArr == linkedArr:
            return True
        else:
            return False