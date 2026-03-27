class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

n1 = ListNode(5)
n2 = ListNode(4)
n3 = ListNode(20)
n4 = ListNode(30)
n5 = ListNode(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1

current = head

while current:
    if current.val > 7:
     print(current.val, end=' ')
    current = current.next