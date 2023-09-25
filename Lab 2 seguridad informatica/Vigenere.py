#Parecido al cifrado cesar pero con la diferencia es que la clave es una cadena.
#lo que hace es tomar la posicion del alfabeto en la clave y la cifra con cesar.
#Y= (XI + ZI)mod T
#Xi posicion letra mensaje a cifrar
#Zi posicion letra clave
#t = numero total letras

Dic = 'abcdefghijklmnopqrstuvwxz'
# Definimos el alfabeto o diccionario

def cifrar (cadena, clave):
    text_cifrar = ''

    i = 0
    for letra in cadena: # procede a usar la formula/ donde busca la letra en el primer ciclo  y luego busca en la clave
        suma = Dic.find(letra) + Dic.find(clave[i % len(clave)]) # % len  por si el largo de la cadena / se modula para que no supere el total de digitos(regresa al principio al llegar a la ultima letra
        modulo = int(suma) % len(Dic)# hacemos lo mismo pero con el diccionario 
        text_cifrar = text_cifrar + str(Dic[modulo])
        i=i+1
    return text_cifrar
        
def descifrar (cadena, clave):
    text_cifrar = '' #variable donde se guarda el texto cifrado

    i = 0
    for letra in cadena:
        suma = Dic.find(letra) - Dic.find(clave[i % len(clave)])  # signo negativo para que Descifre.
        modulo = int(suma) % len(Dic)
        text_cifrar = text_cifrar + str(Dic[modulo]) 
        i=i+1
    return text_cifrar
        
def main () :
    #pedimos la cadena a cifrar.
    cadena = str (input('cadena a cifrar: ')).lower(); #lower para pasar a minusculas/ pedimos el mensaje a cifrar
    clave = str(input('clave:  ' )).lower(); # pedimos la clave a usar para el cifrado
    print (cifrar(cadena,clave)) #entrega el cifrado
    cadena = str (input('cadena a descifrar: ')).lower()
    clave = str(input('clave:  ' )).lower()
    print (descifrar(cadena,clave))
    
if __name__ == '__main__':
    main()

