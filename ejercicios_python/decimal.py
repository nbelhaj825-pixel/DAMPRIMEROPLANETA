import math
def decimalHexadecimal(numero):
    ca="0123456789ABCDEF"
    binario=""
    while(numero>0):
        resto=numero%16
        binario =ca[resto:resto+1]+binario
        numero=numero//16
    return binario


def hexadecimalAdecimal(cadena):
    ca="0123456789ABCDEF"
    n=len(cadena)-1
    suma=0
    j=0
    for i in range(n,-1,-1):
        suma+=ca.find(cadena[i:i+1])*math.pow(16,j)
        j+=1
    return suma


def octalAdecimal(cadena):
    ca="0123456789ABCDEF"
    n=len(cadena)-1
    suma=0
    j=0
    for i in range(n,-1,-1):
        suma+=ca.find(cadena[i:i+1])*math.pow(8,j)
        j+=1
    return suma
    
    



def decimalOctal(numero):
    binario=""
    while(numero>0):
        resto=numero%8
        binario =str(resto)+binario
        numero=numero//8
    return binario

def decimalAbinario(numero):
    binario=""
    while(numero>0):
        resto=numero%2
        binario =str(resto)+binario
        numero=numero//2
    return binario

if __name__ =='__main__':
    print(hexadecimalAdecimal("FF"))
    print(octalAdecimal("377"))
    n=int(input("Dime un numero: "))
    print(f"El numero Hexadecimal es:{decimalHexadecimal(n)}")
    print(f"El numero octal es:{decimalOctal(n)}")
    print(f"El numero binario es:{decimalAbinario(n)}")
    print(f"El numero Decimal es:{hexadecimalAdecimal(n)}")