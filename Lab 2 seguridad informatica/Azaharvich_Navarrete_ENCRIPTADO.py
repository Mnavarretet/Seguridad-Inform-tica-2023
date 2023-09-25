import hashlib

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def leer():
    try:
        with open('mensajedeentrada.txt', 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print("El archivo 'mensajedeentrada.txt' no se encontró.")
        return ""

def escribir(texto):
    try:
        with open('mensajeseguro.txt', 'w') as archivo:
            archivo.write(texto)
    except Exception as e:
        print(f"Error al escribir en el archivo: {str(e)}")

def hashing(texto):
    md5 = hashlib.md5(texto.encode()) 
    return md5.hexdigest()

def rot(mensaje, key, mode):
    mensaje = mensaje.upper()
    traslado = ""
    dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in mensaje:
        if symbol in dic:
            num = dic.find(symbol)
            if mode == "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(dic):
                num -= len(dic)
            elif num < 0:
                num += len(dic)

            traslado += dic[num]
        else:
            traslado += symbol
    return traslado

def vigenere(clave, mensa, accion):
    dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    traducido = []
    indice_clave = 0
    clave = clave.upper()

    for symbol in mensa:
        num = dic.find(symbol.upper())
        if num != -1:
            if accion == 'encrypt':
                num += dic.find(clave[indice_clave])
            elif accion == 'decrypt':
                num -= dic.find(clave[indice_clave])
            num %= len(dic)
            if symbol.isupper():
                traducido.append(dic[num])
            elif symbol.islower():
                traducido.append(dic[num].lower())
            indice_clave += 1
            if indice_clave == len(clave):
                indice_clave = 0
        else:
            traducido.append(symbol)
    return ''.join(traducido)

textor = leer()
hash_md5 = hashing(textor)
texto = rot(hash_md5, 8, 'cifrar')
texto = vigenere('heropassword', texto, 'encrypt')
texto = rot(texto, 12, 'cifrar')
escribir(texto)
