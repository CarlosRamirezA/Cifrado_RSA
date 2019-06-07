import numpy as np
import random

def CalcularExpone(a,k,z):
    exp=1
    xp=a%z
    while(k>0):
        if((k%2)!=0):
            exp=(exp*xp)%z
        xp=(xp*xp)%z
        k=k/2
        return exp

def esPrimo(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generePrim():
    repP = False
    repQ = False
    p=0
    q=0
    while repP==False and repQ ==False and p==q:
        p = int(random.randint(2,100) * (1000-100+1)+100)
        q = int(random.randint(2,100) * (1000-100+1)+100)
        repP = esPrimo(p)
        repQ = esPrimo(q)
    return (p,q)


def decimalBinario(num):
    binario = ''
    while(num//2!=0):
        binario = str(num % 2) + binario
        num = num // 2
    return str(num) + binario

def TextBinario(msj):
    binario = ''
    num = [(ord(char)) for char in msj]
    for i in range(len(num)):
        while num[i] // 2 != 0:
            binario = str(num[i] % 2) + binario
            num[i] = num[i] // 2
        return str(num[i]) + binario

def gcd(a,b):
	residuo = 1
	while(residuo!=0):
		residuo = a%b
		a=b
		b=residuo
	return a

def emcd(a,b):
	if b==0:
		d = a
		x = 1
		y = 0
		return d, x, y
	x1 = 0
	x2 = 1
	y1 = 1
	y2 = 0
	while b > 0:
		q = a//b
		r = a - q*b
		x = x2 - q*x1
		y = y2 - q*y1
		a = b
		b = r
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
	d = a
	x = x2
	y = y2
	return d, x, y

def euclides_extendido(a, b):
    x=0
    y=1
    u=1
    v=0
    while a != 0:
        cociente=b//a
        resto=b%a
        m=x-u*cociente
        n=y-v*cociente

        b=a
        a=resto
        x=u
        y=v
        u=m
        v=n
    mcd = b
    return mcd, x, y

def inver(a, b):
    t=euclides_extendido(a,b)
    if t[0]==1:
        return t[1]%b
    else:
        print("No existe el inverso")

def potencia_modular(a, b, n):
    temp=bin(b)
    temp=temp[2:]
    temp=temp[::-1]
    k=[int(i) for i in temp]
    #print("b=", k)
    b=1
    if all(i==0 for i in k):
        return b
    A=a
    for i in k:
        if i==1:
            b=(A*b)%n
        A=(A**2)%n
    return b


def func_exp(n):
    pot=0
    while n%2==0:
        n=n/2
        pot+=1
    return pot

def jacobi(a,n):
    a1=1
    n1=0
    if(a==0 or a == 1):
        return a
    else:
        e = func_exp(a)
        p = pow(2,e)
        a1=(a/p)
        if(e%2==0):
            s=1
        else:
            if((((n-1)%8)==0)or(((n-7)%8)==0)):
                s=1
            else:
                if((((n-3)%8)==0)or(((n-5)%8)==0)):
                    s=-1
        if((((n-3)%4)==0)and(((a1-3)%4)==0)):
            s=-s
        n1=(n%a1)
        if(a1==1):
            return s
        else:
            return s*jacobi(n1,a1)

def CalcularMultiplicacion(a,b,z):
        respuesta=(a*b)%z
        print(respuesta)
        return respuesta

def CalcularRaiz(p,a):
    print(p)
    print(a)
    aux=0
    auxc=0
    aux3=1
    band=True
    raiz=np.array([],dtype=object)
    if(jacobi(p,a)==-1):
        band=False
        return band,raiz
    while(aux!=-1):
        auxc=auxc+1
        aux=jacobi(auxc,p)
        b=auxc
    s=func_exp(p-1)
    print(s)
    aux_exp=(2**s)
    t=int((p-1)/aux_exp)
    Ia=inver(a,p)
    c=CalcularExpone(b,t,p)
    r=CalcularExpone(a,(int(t+1)/2),p)
    print(r)
    while(aux3<s-1):
        base=r*r*Ia
        print(base)
        exponente=int(2**(s-aux3-1))
        print(exponente)
        d=CalcularExpone(base,exponente,p)
        if((d+1)%p==0):
            r=CalcularMultiplicacion(r,c,p)
        aux3=aux3+1
    c=CalcularExpone(c,2,p)
    raiz=np.append(raiz,[r,-r])
    
    print(band)
    print(raiz)
    return band,raiz

def factores(numero):
    i=3
    factores=np.array([],dtype=int)
    while(numero!=1):
        while(numero%2==0):
            factores=np.append(factores,2)
            numero=numero//2
        while(numero%i==0):
            factores=np.append(factores,i)
            numero=numero//i
        i=i+1
    return factores


def RaizCompuesta(p1,a1):
    raizF=[]
    factorizacion=factores(p1)
    p=factorizacion[1]
    q=factorizacion[0]
    print(p)
    print(q)
    a=a1
    n=p*q
    print(n)
    aux1,raizP1=CalcularRaiz(p,a)
    aux2,raizP2=CalcularRaiz(q,a)
    print(len(raizP2))
     
    if(aux1==False and aux2==False):
        return raizF,False
    else:
        L1=raizP1
        L2=raizP2
        mcd=euclides_extendido(p,q)
        c=mcd[1]
        d=mcd[2]
        r=L1[0]
        s=L2[0]
        x=(r*d*q+s*c*p)%(n)
        y=(r*d*q-s*c*p)%(n)
        raizF.append(x%n)
        raizF.append(-1*raizF[0])
        raizF.append(y%n)
        raizF.append(-1*raizF[2])
        for i in range(4):
            if(raizF[i]<0):
                raizF=raizF+n
    return raizF,True

def Legendre(a, p):
    y=pow(int(a),int((p-1)/2),p)
    return y

def Multiplicativo(n):

    multiplicativo=np.array([],dtype=int)
    b=n

    for i in range(n):
        x=i
        while(n!=0):
            r=x%n
            x=n
            n=r
            if(x==1):
                multiplicativo=np.append(multiplicativo,i)
        n=b
    return multiplicativo
        


