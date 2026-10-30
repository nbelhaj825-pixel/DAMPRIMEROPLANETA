

castellano=["Blanco","Negro"]
ingles=["white","Black"]

while(True):
    palabra=input("Dime una palabra : ")
    if (palabra=="salir"): break
    
    if (castellano.count(palabra)==0):
        word=input("Dime la traduccion : ")
        castellano.append(palabra)
        ingles.append(word)
    else:
        n=castellano.index(palabra)
        print(f'la palabra {palabra} se traduce {ingles[n]}')

print(castellano)
print(ingles)