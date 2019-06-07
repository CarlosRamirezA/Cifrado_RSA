import Modulos as M
from random import randrange as rdm
import numpy as np


def Grupo_Cifrado(msj,n):
    msj=msj.replace(' ','').upper()
    base=len(abecedario)

    mnsj_bloques=np.array([],dtype=object)
    for i in range(len(msj)):
        mnsj_bloques=np.append(mnsj_bloques,[msj[i]])
       
    print(mnsj_bloques)
    mnsj_bloques_decimal=np.array([],dtype=object)
    for i in range(len(mnsj_bloques)):
        mnsj_bloques_decimal=np.append(mnsj_bloques_decimal,[abecedario.find(mnsj_bloques[i])])
    
    print(mnsj_bloques_decimal)
    k=np.array([],dtype=int)
    for i in range(len(mnsj_bloques_decimal)):
        if(i%2==0):
            if(i!=len(mnsj_bloques_decimal)-1):
                z=mnsj_bloques_decimal[i]*100+mnsj_bloques_decimal[i+1]
                k=np.append(k,[z])
            else:
                if(mnsj_bloques_decimal[i]!=0):
                    z=mnsj_bloques_decimal[i]*100+(mnsj_bloques_decimal[i]-1)
                    k=np.append(k,z)
                else:
                    k=np.append(k,[0])
    return k


def generador_claves(p,q):
    n = p*q 
    phi = (p-1)*(q-1)
    e = rdm(1,phi)
    g = M.gcd(e, phi)
    while g!= 1:
        e = rdm(1, phi)
        g = M.gcd(e, phi)
    
    d =M.inver(e,phi) 
    return (n),(e),(d)

def encriptar_RSA(msn,publica,n):
    j=np.array([],dtype=int)
    for i in range(len(msn)):
        c=M.potencia_modular(msn[i],publica,n)
        j=np.append(j,c)
    return j

def desencriptar_RSA(msn,privada,n):
    j=np.array([],dtype=int)
    for i in range(len(msn)):
        c=M.potencia_modular(msn[i],privada,n)
        j=np.append(j,c)

        letra=np.array([],dtype=int)
    print(j)
    for i in range(len(k)):
        letra=np.append(letra,int(j[i]/100))
        letra=np.append(letra,j[i]%100)
    aux=""
    for i in range(len(letra)):
     aux=aux+abecedario[letra[i]]
    return aux

abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

p =531872289054204184185084734375133399408303613982130856645299464930952178606045848877129147820387996428175564228204785846141207532462936339834139412401975338705794646595487324365194792822189473092273993580587964571659678084484152603881094176995594813302284232006001752128168901293560051833646881436219
q =203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123

n,publica,privada=generador_claves(p,q)


msj = input("ingrese su msj : ")
k=Grupo_Cifrado(msj,n)
    
cifrado=encriptar_RSA(k,publica,n)

print(cifrado)

descifrado=desencriptar_RSA(cifrado,privada,n)

print(descifrado)




