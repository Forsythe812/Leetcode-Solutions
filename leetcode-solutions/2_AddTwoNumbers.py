class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None
    

# Creating node1 linkedlist nodes
node1_1= ListNode(2)
node1_2= ListNode(4)
node1_3= ListNode(3)

# Creating node2 linkedlist nodes
node2_1= ListNode(5)
node2_2= ListNode(6)
node2_3= ListNode(4)

# Assigning node1 next values
node1_1.next = node1_2
node1_2.next = node1_3

# Assigning node2 next values
node2_1.next = node2_2
node2_2.next = node2_3

testValue_node1 = node1_1
testValue_node2 = node2_1

# # Printing elements of node 1
# print(5*'-' + 'Elements of node 1' + 5*'-')
# while testValue_node1 :
#     print(testValue_node1.data)
#     testValue_node1 = testValue_node1.next

# # Printing elements of node 2
# print(5*'-' + 'Elements of node 2' + 5*'-')
# while testValue_node2 :
#     print(testValue_node2.data)
#     testValue_node2 = testValue_node2.next

def AddTwoNumbers (l1,l2) :
    carry = 0
    totalSum = 0
    newList = ListNode(0)
    temp = newList

    while l1 or l2 or carry :
        if l1:
            totalSum += l1.data
            l1 = l1.next
        if l2 :
            totalSum += l2.data
            l2 = l2.next
        totalSum += carry
        carry = totalSum // 10
        temp.next = ListNode(totalSum % 10)
        print(temp.next)
        temp = temp.next
        totalSum = 0
    print(newList.next)
    return newList.next
        
print(AddTwoNumbers(node1_1,node2_1))
    


