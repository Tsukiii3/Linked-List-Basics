'''
def pesquisa_binária(lista,item):
    baixo = 0
    tent = 0
    alto = (len(lista)-1)

    while baixo <= alto:
        meio = (baixo+alto)//2
        chute = lista[meio]
        tent += 1
        if chute == item:     #Aqui foram 2 tentativas
            return meio, tent
        if chute > item:
         alto = meio-1
        else:
         baixo = meio+1
    return None, tent



minha_lista =[1,3,4,5,6,7]
print(pesquisa_binária(minha_lista,6)) '''

'''
def buscaSimples(lista, item):
    tent = 0
    for i in range(len(lista)):   #Aqui foram 5 tentativas
        tent +=1
        if lista[i] == item:
            return i, tent

    return None, tent

print(buscaSimples([1,3,4,5,6,7], 6))  '''

'''

def ordernar_selecao(arr):
    novo = []
    copia = arr [:]

    while len(copia) > 0:
        menor = 0
        for i in range(len(copia)):
            if copia[i] < copia[menor]:
                menor = i
        novo.append(copia[menor])
        copia.remove(copia[menor])
    return novo

print(ordernar_selecao([7,9,4,3,6,4,2]))  '''

'''
def busca_maior(lista):
    maior = lista[0]

    for num in lista:
        if num > maior:
            maior = num
    return maior

print(busca_maior([1,8,9,3,4,2])) '''

'''
def soma(lista):
    soma = 0
    for num in lista:
        soma+= num
    return soma

print(soma([1,8,9,3,4,2])) '''

'''

def jogo_adivinhacao():
    baixo = 0
    alto = 100

    while True:
        palp = (baixo + alto) // 2
        print(f'Seu número é {palp}')

        resp = input('Digite "maior", "menor" ou "acertou" ')
        if resp == 'acertou':
            print('Você acertou!')
            break
        if resp == "maior":
            baixo = palp -+1
        if resp == "menor":
            alto = palp -+1

print(jogo_adivinhacao()) '''

def menor(lista):
    menor = lista[0]
    indice = 0
    novo = lista[:]
    for num in lista:
        if num < menor:
            menor = num
    for i in range(len(lista)):
        if lista[i] == menor:
            indice = i
    novo.append(menor)
    return menor, indice, novo

print(menor([5,3,6,2,10]))





