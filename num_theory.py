"""
Prime check and fast super exponential algorithms
"""

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

def superExp(a,n,tupl):
    t,f=tupl
    if n==0:
        return 1
    if (t==0 and f==0):
        return 0
    elif f==0 :
        nt=t-1
        nf=f
    else:
        nt=t+1
        nf=f-1
    return repeatedSquaring(a,superExp(a,n-1,(nt,nf)),(2**t)*(5**f))

def superExpWrapper(a,n,digits):
    return superExp(a,n,(digits,digits))


print(superExpWrapper(1707,1783,16))

for i in [67280421310721,170141183460469231731687303715884105721,(2**2281)-1,(2**9941)-1,(2**19939)-1]:
    print(fermat(i,10))
#(True,False,True,True,False)
