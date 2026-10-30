




if __name__== '__main__':
       n=int(input("Dime nº de numeros que quieres: "))
       suma=0

       for i in range(n):
              numero=float(input("Dime un numero : "))
              suma += numero #suma = suma + numero
              numero = n+1
              media = numero / n



              if (i==0):
                     maximo=numero
                     minimo=numero
                     cmaximo=1
                     cminimo=1
              else:
                  
                     if(numero>maximo):
                       maximo=numero
                       cmaximo=1
                     elif (numero==maximo):
                       cmaximo += 1 #cmaximo=cmaximo+1

                     if(numero<minimo):
                            minimo=numero
                            cminimo=1
                     elif (numero==minimo):
                            cminimo += 1    #cminimo=cminimo+1    

print(f'La media es : {media/n:.2f}')
print(f'El maximo : {maximo} y nº veces : {cmaximo}')
print(f'El minimo : {minimo} y nº veces : {cminimo}')
       
       
