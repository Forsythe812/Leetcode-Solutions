def deleteDuplicates(head):
    if head == None:
        return head
        
    current = head.next
    prev = head
 
    while current :
        if current.val == prev.val :
            prev.next = current.next
            #current = current.next
        else :
            prev = prev.next
            #current = current.next
        current = current.next
        
    return head
