'''
def recursiva(i):
    print(i)
    if i <= 1:
        return
    else:
        recursiva(i-1)

print(recursiva(5)) '''

'''
def soma(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + soma(arr[1:]) 

print(soma([4,5,6,9])) '''

'''
def maior(arr):
    maior = 0
    for item in arr:
        if item > maior:
            maior = item
    return maior

print(maior([0,5,10,3,89,2])) '''

'''
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([3,4,7,9,0,3,])) '''

'''
def tamanho_lista(lista):
    tamanho = 0
    for i in lista:
        tamanho += 1
    return tamanho
print(tamanho_lista([4,5,6,9]))  '''

#Versão Recursiva

def tamanho_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + tamanho_lista(lista[1:])

print(tamanho_lista([4,5,6,9]))



