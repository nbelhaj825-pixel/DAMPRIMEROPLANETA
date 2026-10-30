n=int(input("Itroduce el numero de mes"))
print(n)

if n<=3:
    print ("primer trimestre")
elif n>=4 and n<=6:
    print ("segundo trimestre")
elif n>=4 and n<=9:
    print ("tercer trimestre")
elif n>=4 and n<=12:
    print ("cuarto trimestre")
else:
    print("El numero de mes tiene que estar entre 1 y 12")

print("Final del programa")
