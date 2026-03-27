# Linked Lists - Exercícios Básicos em Python

Este repositório contém exercícios simples para praticar **Listas Encadeadas (Linked Lists)** em Python.

## 📚 Conteúdo

### 1. Imprimir uma lista encadeada

Percorre a lista e imprime os valores no formato:

```
5 -> 4 -> 20 -> 30 -> 7
```
Lista Completa:
````
n1 = ListNode(5)
n2 = ListNode(4)
n3 = ListNode(20)
n4 = ListNode(30)
n5 = ListNode(7)
````
Lógica usada:
```
while current:
    print(current.val, end=' ')
    current = current.next
```

---

### 2. Maior e menor valor

Percorre a lista para encontrar:

* Maior valor

Lógica usada: 
```
while current:
    if maior < current.val:
        maior = current.val
    print(current.val, end=' -> ')
```
    
* Menor valor

Lógica usada:
```
if menor > current.val:
        menor = current.val
    current = current.next
```

Lista Completa:
```
n1 = ListNode(5)
n2 = ListNode(3)
n3 = ListNode(25)
n4 = ListNode(8)
```

Exemplo de saída:

```
O maior valor da lista é 25
O menor valor da lista é 3
```

---

### 3. Números pares e ímpares

Separa os valores da lista em:

* Números pares

Lógica usada:
````
while current:
    if current.val % 2 == 0:
        print(current.val, end=' -> ')
    current = current.next
````

* Números ímpares

Lógica usada:
```
while current:
    if current.val % 2 != 0:
        print(current.val, end=' -> ')
    current = current.next
```

Lista Completa:
````
n1 = ListNode(5)
n2 = ListNode(3)
n3 = ListNode(25)
n4 = ListNode(8)
````

---

### 4. Inverter a lista encadeada

Inverte a ordem dos nós da lista.

Exemplo:

```
Antes: 5 -> 3 -> 25 -> 8  
Depois: 8 -> 25 -> 3 -> 5
```
Lista Completa:
```
n1 = ListNode(5)
n2 = ListNode(3)
n3 = ListNode(25)
n4 = ListNode(8)
```
Lógica usada: 
```
while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

head = prev

current = head

while current:
    print(current.val, end=' -> ')
    current = current.next
```
---

## 🧠 Estrutura utilizada

Classe básica de nó:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## 🚀 Objetivo

Praticar conceitos fundamentais como:

* Ponteiros (referências)
* Percorrer listas
* Manipulação de nós
* Lógica de algoritmos

---

## ✍️ Autor

Projeto feito para estudo de estruturas de dados.
