if __name__ == '__main__':
    maximo=-1
    minimo=11
    cmaximo=cminimo=0

    for i in range(1,6):
        nota=float(input("Dime la nota "))
        
        if (nota>maximo):
            maximo=nota
            cmaximo=1

        elif (nota==maximo):
            cmaximo+=1

        if (nota<minimo):
            minimo=nota
            cminimo=1

        elif (nota==minimo):
            cminimo+=1

        

        
    
    print(f'maximo:{maximo}\nminimo:{minimo}')
    print(f'repetidos maximo:{cmaximo}\nrepetidos minimo:{cminimo}')