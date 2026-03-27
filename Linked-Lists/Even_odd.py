class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

n1 = ListNode(5)
n2 = ListNode(3)
n3 = ListNode(25)
n4 = ListNode(8)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1
current = head

print('Even numbers: ')
while current:
    if current.val % 2 == 0:
        print(current.val, end=' -> ')
    current = current.next

current = head

print('\nOdd numbers: ')
while current:
    if current.val % 2 != 0:
        print(current.val, end=' -> ')
    current = current.next