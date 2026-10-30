n=float(input("Introduce la nota"))

#float decimal numbers

if (n<5):
    print ("Suspenso")
elif (n>=5 and n<=6):
    print("Aprobado")
elif (n>=6 and n<=7):
    print("Bien")
elif (n>=7 and n<=9):
    print("Notable")
elif (n>=9 and n<=10):
    print("Sobresaliente")

elif (n<0 or n>10):
    print("Fuera de rango")

print("Final del programa")