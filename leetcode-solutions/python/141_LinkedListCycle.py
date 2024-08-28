def hasCycle(head):
        
    if head == None or head.next == None :
        return False
        
    prev = head
    current = head.next
        
    while current.next != None :
            
        # Using the 2 pointers, current moves 2 step while prev move 1 step
        # So that if it's a circle current will be able to chase and meet with prev
        current = current.next.next
        prev = prev.next
            
        # If current and prev met in the chase return True
        if current == prev :
            return True
            
        # When it reached at the end of LinkedList element 
        # and next is None return False
        if current == None or current.next == None : 
            return False
          
    return False
        