#En esta funcion a cada valor de x que ingresaba la funcion rot, verifica cada posicion y la modula para que calzara en el alfabeto
def customAbs(x):
    if x >= 0:
        return x % 26
    return 26 + x

#el n aqui significa cuantos espacios estoy rotando. Ocupa norma Asis obteniendo el numero en el alfabeto para mayusculas y minusculas.
def rot(r, n):
    if r >= 'a' and r <= 'z':
        return chr(customAbs(ord(r) + n - 97) + 97)

    if r >= 'A' and r <= 'Z':
        return chr(customAbs(ord(r) + n - 65) + 65)
    return str(r)

#Este Rot realiza el encriptado final 
def Rot(cadena, n):
    newString =''
    for r in cadena:
        newString = newString + rot(r, n)
    return newString





