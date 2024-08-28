# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None :
            return True
        
        current = head
        arr = []
        
        while current :
            arr.append(current.val)
            current = current.next
        
        current = head
        
        while current :
            if current.val != arr[-1] :
                return False
            arr.pop()
            current = current.next
        return True