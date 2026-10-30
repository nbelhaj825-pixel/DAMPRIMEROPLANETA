


def esPrimo(n):
    for i in range (2,n):
        if (n%i==0): return False 
    return True

if __name__ == '__main__':
    numero=int(input("Introduce el numero"))
    c=0
    while(c<5):
        if (esPrimo(numero)):
            c+=1
            print(f'{c} {numero}')
        numero+=1
    


