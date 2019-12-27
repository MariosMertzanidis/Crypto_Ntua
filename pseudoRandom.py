"""
BBS pseudo random algorithm and checks
"""

import random as rnd
import math
import sys

def repeatedSquaring(a,n,m):
    x=a%m
    y=1
    while (n>0) :
        if (n%2 != 0):
            y=(y*x)%m
        x=(x**2)%m
        n=n//2
    return y

def fermat(a,iter):
    w=2
    for _ in range(iter):
        if  (repeatedSquaring(w,a-1,a) != 1) :
            return False
        w+=1
    return True

def create_bbs_primes():
    p = rnd.randint(2**20,2**21)
    q = rnd.randint(2**20,2**21)
    while(1):
        if (fermat(p,10) and p%4==3 ):
            break
        p+=1
        if (p==2**21):
            p=2**20
    while(1):
        if (fermat(q,10) and q%4==3 ):
            break
        q+=1
        if (q==2**21):
            q=2**20
    if p!=q:
        return p,q
    else:
        return create_bbs_primes()

def parity(n):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return abs(parity)

def bbs(bits,seed,proc=lambda n : n%2):
    s=seed
    out=""
    p,q=create_bbs_primes()
    n=p*q
    for _ in range(bits):
        s=repeatedSquaring(s,2,n)
        out=out+str(proc(s))
    return out


def countOnes(s):
    n=0
    for i in s:
        if i == "1":
            n+=1
    return n


def consOnes(s):
    out=0
    temp=0
    for i in s:
        if i == "1":
            temp+=1
        else:
            if out < temp :
                out = temp
            temp=0
    return out

def runsTest(iter,proced=lambda n : n%2):
    y=0
    for _ in range(iter):
        bits=rnd.randint(10000,100000)
        y+=abs((math.log2(bits+2)-1)-consOnes(bbs(bits,rnd.randint(0,2**21),proc=proced)))
    return y/iter

def freqMonobit(iter,proced=lambda n : n%2):
    y=0
    for _ in range(iter):
        y+=countOnes(bbs(1024,rnd.randint(0,2**21),proc=proced))
    return(y/(1024*iter))
'''
print("Monobit Frequency Test:")
print("Modulo 2:",freqMonobit(int(sys.argv[1])))
print("Parity:",freqMonobit(int(sys.argv[1]),parity))
print("Longest Runs:")
print("Modulo 2:",runsTest(int(sys.argv[1])))
print("Parity:",runsTest(int(sys.argv[1]),parity))
'''

def calcNum(s):
    y=0
    for n,i in enumerate(s):
        if i=="1":
            y+=2**(len(s)-n-1)
    return y

def pi4(iter,bits=8):
    inside=0
    for _ in range(iter):
        x=calcNum(bbs(bits,rnd.randint(0,2**21)))
        y=calcNum(bbs(bits,rnd.randint(0,2**21)))
        if(((255/(2**bits-1))*x-127.5)**2+((255/(2**bits-1))*y-127.5)**2<=127.5**2):
            inside+=1
    return  inside/iter



print("pi/4",math.pi/4)
print("9 bits",pi4(10000,9))
print("11 bits",pi4(10000,11))
print("13 bits",pi4(10000,13))


#print("Real pi/4",math.pi/4," Calculated pi/4:",pi4(1000))


def bbs_period():
    rep=s=15
    out=0
    p,q=11,17
    n=p*q
    for i in range(100):
        if i==5:
            rep=s
            out=0
        s=repeatedSquaring(s,2,n)
        out+=1
        if s==rep:
            break
    return out


#print("p=11,q=17 period BBS:",bbs_period())
