lista=[]
lista.append(10)
lista.append(20)
lista.extend([10, 11, 12])
print(lista)
lista[0]=555
print(lista)


lista.insert(1,77777)


for i in range(0,len(lista)):
    print(i,lista[i])


lista.insert(0,8888888)  #insertar al principio de la lista
lista.insert(len(lista),999999)

print (lista)


n=lista.index(11) # si no existe da error
print(n)

a=lista.remove(10)
print(a)