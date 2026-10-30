def letradni(numero):
    cadena="TRWAGMYFPDXBNJZSQVHLCKE"
    n=numero%23
    return cadena[n]


def letranie(texto):
    texto=str("XYZ".index(texto[0]))+texto[1:]
    return  letradni(int(texto))

def letraniedni(texto):
    cadena="TRWAGMYFPDXBNJZSQVHLCKE"
    n="XYZ".find(texto[0])
    if (n==-1):
        m=int(texto)%23
    else:
        m=int(str(n)+texto[1:])%23
         
    
        return cadena[m]

if __name__ == '__main__':
        dni=int("50691319")
        print(dni,letradni(dni))
        nie="Z5034722"
        print(nie,letranie(nie))