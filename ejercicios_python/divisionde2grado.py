import math

def soluciones(a,b,c):
    discriminante=math.pow(b,2)-(4*a*c)
    
    if(discriminante==0):
        print("La raiz es "+( -b/(2*a) ))
    else:
        x1= (-b+math.sqrt(discriminante))/(2*a)
        x2= (-b-math.sqrt(discriminante))/(2*a)
        print(f'las raices son {x1} y {x2}')


if __name__ == '__main__':

    va=float(input("Dime un numero: "))
    if va == 0:
        raise ValueError("Error")
    vb=float(input("Dime un numero: "))
    if vb == 0:
        raise ValueError("Error")
    vc=float(input("Dime un numero: "))
    if vc == 0:
        raise ValueError("Error")
    
    soluciones(va,vb,vc)
    
  


    



    
    