def pesquisa_binária(lista,item):
    baixo = 0
    alto = (len(lista)-1)

    while baixo <= alto:
        meio = (baixo+alto)//2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
         alto = meio-1
        else:
         baixo = meio+1
    return None

minha_lista =[1,3,4,5,6,7]
print(pesquisa_binária(minha_lista,6))


