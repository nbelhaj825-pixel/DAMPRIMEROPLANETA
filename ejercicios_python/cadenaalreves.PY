def reverso(cadena):
    salida=""
    for i in range(len(cadena)-1,-1,-1):
        salida +=cadena[i]
    return salida

print (reverso("Hasta mañana a las 8"))
    