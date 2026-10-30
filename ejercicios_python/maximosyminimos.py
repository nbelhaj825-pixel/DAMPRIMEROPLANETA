






if __name__ == '__main__':
    for i in range(1,6):
        numero=float(input("Introduce un numero"))
        if (i==1):
            maximo=minimo=numero
        else:
            if (numero>maximo):
                maximo=numero
            elif (numero<minimo):
                minimo=numero
    print(f'El minimo : {minimo}\nEl maximo : {maximo}')

