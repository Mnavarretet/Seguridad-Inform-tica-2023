import hashlib

def leer():
    archivo=open('mensajedeentrada.txt.','r')
    a=archivo.read()
    archivo.close()
    return a

def escribir(texto):
    final=texto
    archivo=open('mensajeseguro.txt','w')
    archivo.write(final)
    archivo.close()

def hashing(texto):
    md5 = hashlib.md5(texto.encode()) 
    return md5.hexdigest()

def rot (mensaje, key, mode):
    mensaje    = mensaje.upper()
    traslado = ""
    dic    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in mensaje:
        if symbol in dic:
            num = dic.find(symbol)
            if mode == "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    return translated

def vigenere(clave,mensa,accion):
    dic = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    traducido=[]
    indice_clave=0
    clave=clave.upper()

    for symbol in mensa:
        num=dic.find(symbol.upper())
        if num!=-1:
            if accion=='encriptar':
                num+=dic.find(clave[indice_clave])
            elif accion=='descifrar':
                num-=dic.find(clave[indice_clave])
            num%=len(dic)
            if symbol.isupper():
                traducido.append(dic[num])
            elif symbol.islower():
                traducido.append(dic[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)

textor=leer()
hash_md5=hashing(textor)
texto=rot(hash_md5,8,'cifrar')
texto=vigenere('heropassword',texto,'encriptar')
texto=rot(texto,12,'cifrar')
escribir(texto)


