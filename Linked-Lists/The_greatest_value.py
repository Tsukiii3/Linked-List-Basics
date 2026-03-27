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
maior = head.val
menor = head.val
current = head
while current:
    if maior < current.val:
        maior = current.val
    print(current.val, end=' -> ')
    if menor > current.val:
        menor = current.val
    current = current.next
print(f'\nThe highest value is {maior}')
print(f'The smallest value is {menor}')