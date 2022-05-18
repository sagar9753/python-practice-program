import time as t

def fact_iter(x):
    f=1

    for i in range(x,0,-1):
        f=f*i

    return f

def fact_recur(x):
    f=1

    if x==0 or x==1:
        return f
    else:
        f=x*fact_recur(x-1)
        return f


for i in range(5,100,5):
    print(i)
