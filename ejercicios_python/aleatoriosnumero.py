import random 

def añadir():
    global lista
    for i in range (20):
        n=random.radient(10,50)
        lista.append(n)
        #print(f'{i+1} {n}')

def calcular():
    global lista
    maximo=minimio=cmaximo=cminimio=suma=0
    
    for i in range(len(lista)):
        suma +=lista[i]
        if (i==0):
            maximo=minimio=lista[i]
            cmaximo=cminimo=1
        else:
             #=================================     
            if(lista[i]>maximo):
               maximo=lista[i]
               cmaximo=1
            elif (lista[i]==maximo):
                cmaximo += 1 #cmaximo=cmaximo+1
            #==================================
            if(lista[i]<minimo):
                minimo=lista[i]
                cminimo=1
            elif (lista[i]==minimo):
                cminimo += 1    #cminimo=cminimo+1 
    print(f'La media es : {suma/len:(lista):.2f}')
    print(f'El maximo : {maximo} y nº veces : {cmaximo}')
    print(f'El minimo : {minimo} y nº veces : {cminimo}')


if __name__ == '__main__':
    lista=[]
    añadir()
    print(lista.sort())
    print(lista)
    calcular()

    



        




