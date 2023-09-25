from ctypes.wintypes import PLARGE_INTEGER
import hashlib 
import rot
import vigenere

def LeerOriginal():
    archivo = open('mensajedeentrada.txt','r')
    aux = archivo.read()
    archivo.close()
    return aux

def LeerReceptor():
    archivo = open('mensajeseguro.txt','r')
    pos = archivo.read()
    archivo.close()
    return pos

def escribir(texto):
    texto = texto
    archivo = open('mensajeseguro.txt','w')
    archivo.write(texto)
    archivo.close()

def hashing(texto):
    md5 = hashlib.md5(texto.encode()) 
    return md5.hexdigest()

def rot (texto,llave,modo):
    texto = texto.upper()
    traduccion = ""
    dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in texto:
        if i in dic:
            aux = dic.find(i)
            if modo ==   "cifrar":
                aux = aux + llave
            elif modo == "descifrar":
                aux = aux - llave

            if aux >= len(dic):
                aux -= len(dic)
            elif aux < 0:
                aux += len(dic)

            traduccion += dic[aux]
        else:
            traduccion += i
    return traduccion

texto = LeerReceptor().upper()
textohash = hashing(texto)
print(textohash)




original = LeerOriginal()
print(texto)

texto = rot(texto,12,"descifrar")
print(texto)

texto = vigenere("passwd",texto,'descifrar')
print(texto)

texto = rot(texto,8,'descifrar')
print(texto)

texto = texto.lower()
hash_de_verificacion = hashing(original)

#Verificacion
if hash_de_verificacion == texto:
    print('El mensaje es seguro, no ha sido modificado')
else:
    print('el mensaje ha sido vulnerado')
