from collections import deque
'''
grafo = {
  "voce": ["alice", "bob"],
  "bob": ["anuj", "peggy"],
  "alice": ["peggy"],
  "anuj": [],
  "peggy": []
}

fila = deque()
fila += grafo["voce"]

verificados = []

while fila:
    pessoa = fila.popleft()

    if pessoa not in verificados:
        if pessoa[-1] == "m":
            print("É vendedor!")
            break
        else:
            fila += grafo[pessoa]
            verificados.append(pessoa) '''

#Exericio 4 e 5, Criar um grafo e FAZER UMA PROCURA BFS
grafo = {
    'A': ['B' 'C'],
    'B': ['D'],
    'C': ['E']
}

fila = deque()
fila += grafo['A']

verificados = []
while fila:
    letra = fila.popleft()
    if letra not in verificados:
        if letra == 'E':
            print('Achei o E')
            break
        else:
            fila += grafo[letra]
            verificados.append(letra)


