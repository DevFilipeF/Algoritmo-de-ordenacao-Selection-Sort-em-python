import random
import math

def randomLista(qtd):
    global lista
    global sorteado
    cont = 0
    lista = []    
    while cont < qtd:
        sorteado = random.randint(1,100)       
        while sorteado in lista:
            sorteado = random.randint(1,100) 
        else:
            lista.append(sorteado)
        cont += 1
    return sorted(lista)

listaNum = randomLista(10)
print("Lista Desordenada: ", lista)
print("Lista Ordenada: ", listaNum, len(listaNum))

for _ in range(0):
    
    
    for chave, val in enumerate(listaNum):
        if sorteado < val:
            listaNum.insert(chave, sorteado)
            break
    else:
        listaNum.append(sorteado)
    print("Lista Atual: ", listaNum)








    
    
    
    

