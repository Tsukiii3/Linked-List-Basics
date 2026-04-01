'''
caderno = dict()

caderno['Controle'] = 499
caderno['Switch 2'] = 4500
caderno['Switch OLED'] = 2100
caderno['Play 5'] = 3200
print(caderno)

p = str(input("Quanto que é o preço do: "))

if p not in caderno:
    print('Não temos esse item')
else:
    print(caderno[p]) '''

#Exercicio 01 Criar um dict com nome e idade, digite um nome e retorne a idade

'''
pessoa = {
    'Rafael': 19,
    'Pedro': 25,
    'Leonardo': 27,
    'Higor': 18
}

c = str(input("Você quer saber de quem? : "))

if c not in pessoa:
    print('Não conheço!')
else:
    print(f'ATAAAAA PO o {c} tem {pessoa[c]} anos pô!') '''

#Exercicio 02 verificar se o número está duplicado
'''
lista = [1, 2, 3, 4, 5, 2]
sem_rep = []


for i in lista:
    if i not in sem_rep:
        sem_rep.append(i)
    else:
        print(f'o valor {i} já existe na lista')
print(sem_rep)

#Versão com O(1)
lista = [1, 2, 3, 4, 5, 2]
vistos = {}

for i in lista:
    if i in vistos:
        print(f'o valor {i} já existe na lista')
    else:
        vistos[i] = True '''

#Exercicio 03 verificar quantas vezes a palavra aparece

'''
lista = ["maçã", "banana", "maçã", "uva"]
contador = {}

for palavra in lista:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print(contador)  

#Sei fazer não! '''

#Dada uma lista de números, retorne True se existir duplicado, senão False.


def tem_duplicado(lista):
    vistos = set()

    for num in lista:     #Usando Hash para verificar se tem algum número duplicado
        if num in vistos:
            return True
        vistos.add(num)
    return False

print(tem_duplicado([4,8,9,2,4]))

def primeiro_repetido(lista):
    vistos = set()

    for num in lista: #Usando Hash para verificar o primeiro valor número duplicado
        if num in vistos:
            return num
        vistos.add(num)
    return None

print(primeiro_repetido([4,8,9,2,4]))



