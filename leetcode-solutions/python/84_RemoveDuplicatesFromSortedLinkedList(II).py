class ListNode:
    def __init__ (self, x) :
        self.val = x
        self.next = None

def deleteDuplicates(head):
    if head == None:
        return head
    
    curr = head
    prev = slow = ListNode(-1)
    prev.next = curr
        
    while curr and curr.next :
        #Until all linked list that has the same element are visited
        if curr.val == curr.next.val :  
            while(curr and curr.next and curr.val == curr.next.val) : 
                # While curr, curr.next EXIST and CURRENT.VALUE is equals to CURRENT.NEXT.VALUE,
                # Keep going to the next element
                curr = curr.next
            # Move to the next element when the current element and the next element doesnt have the next value
            # and assigning slow.next to current.next element
                
            slow.next = curr.next
            curr = curr.next
        else :
            slow = slow.next
            curr = curr.next
                
    return prev.next