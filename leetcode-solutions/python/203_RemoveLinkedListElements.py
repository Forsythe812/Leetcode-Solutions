class ListNode:
    def __init__ (self, x) :
        self.val = x
        self.next = None

def removeElements(head,val):
        if head == None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        temp = dummy.next
        
        while temp:
            if (temp.val == val) :
                if temp.next != None :
                    prev.next = temp.next
                else :
                    prev.next = None
                    temp = None
                    break
            else :     
                prev = prev.next
            temp = temp.next        
        return dummy.next

# def removeElements(self, head: ListNode, val: int) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head
#         prev = dummy
#         temp = dummy.next
#         while temp :
#             if (temp.val == val) :
#                 prev.next = temp.next
#             else :
#                 prev = prev.next
#             temp = temp.next
#         return dummy.next