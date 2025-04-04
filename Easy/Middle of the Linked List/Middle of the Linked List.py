# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        returnCycle = head
        length = 0
        while current:  # While there is a node
            length += 1
            current = current.next  # Move to the next node
        if length % 2 == 1:
            middle = int((length+1)/2)
        else:
            middle = int((length/2) + 1)
        print(middle)
        count = 0
        while returnCycle:  # While there is a node
            count+=1
            if count == middle:
                return returnCycle
            returnCycle = returnCycle.next  # Move to the next node
        return None

head = ListNode(65)
head.next = ListNode(66)
head.next.next = ListNode(26)
head.next.next.next = ListNode(77)
head.next.next.next.next = ListNode(96)
head.next.next.next.next.next = ListNode(86)
head.next.next.next.next.next.next = ListNode(11)
head.next.next.next.next.next.next.next = ListNode(21)
head.next.next.next.next.next.next.next = ListNode(13)
head.next.next.next.next.next.next.next.next = ListNode(80)

solution = Solution()
print(solution.middleNode(head))