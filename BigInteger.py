def write(a):
    for i in reversed(a):
        print(i,end="")
def norm(a,b):
    if len(a)< len(b):
        a,b = b,a
    return a,b
def plus(a,b):
    a,b = norm(a,b)
    per = 0
    c = []
    for i in a:
        c.append(i)
    for i in range(len(b)):
        t = a[i] + b[i] + per
        c[i] = t % 10
        per = t // 10
    if per:
        if i == len(a) - 1:
            c.append(per)
        else:
            c[i+1]+=per
    return c
def graterEqvLower(a,b):
    l1 = len(a)
    l2 = len(b)
    if l1 > l2:
        return 1
    if l1 < l2:
        return -1
    for i in range(l1 - 1,-1,-1):
        if a[i] > b[i]:
            return 1
        if a[i] < b[i]:
            return -1
    return 0
def minus(a,b):
    zaem = 0
    c = []
    for i in a:
        c.append(i)
    for i in range(len(b)):
        t = a[i] - b[i] - zaem
        if t < 0:
            c[i] = t + 10
            zaem = 1
        else:
            c[i] = t
            zaem = 0
    while zaem:
        i+=1
        t = a[i] - zaem
        if t < 0:
            c[i] = t + 10
        else:
            c[i] = t
            zaem = 0
    i = len(a) - 1
    while i >= 0 and c[i] == 0:
        i-=1
    k = []
    for j in range(i + 1):
        k.append(c[j])
    if not len(k):
        return [0]
    return k
def umnozhNum(a,x):
    perehod = 0
    b = []
    for i in range(len(a)):
        t = a[i] * x + perehod
        b.append(t%10)
        perehod = t//10
    if perehod:
        b.append(perehod)
    return b
def umnozh10(a, count):
    if count > 0:
        b = [0]*count
        for i in a:
            b.append(i)
        return b
    return a
def umnozh(a,b):
    a,b = norm(a,b)
    s = []
    for i in range(len(b)):
        s = plus(s, umnozh10(umnozhNum(a, b[i]), i))
    return s
def pow(a,x):
    if x > 0:
        t = []
        for i in a:
            t.append(i)
        for i in range(x - 1):
            t = umnozh(t,a)
        return t
    print("VALUE ERROR in pow: x must be grater than zero, but x =",x)
    exit()
def delNum(a,x):
    # minus = (x < 0)
    x = abs(x)
    b = []
    t = 0
    for i in range(len(a)-1,-1,-1):
        t *= 10
        t += a[i]
        c = t // x
        b.append(c)
        t = t - c * x
    c = []
    # ost = t / x
    # if abs(ost) > 0.000001:
    #     c.append(ost)
    i = 0
    l = len(b)
    while i < l and b[i] == 0:
        i+=1
    for j in range(l-1,i-1,-1):
        c.append(b[j])
    return c
def koren(a):
    l,r = [0],umnozh10([1],(len(a)-1)//2 + 1)
    while graterEqvLower(minus(r,l),[1]) == 1:
        mid = delNum((plus(l,r)),2)
        t = graterEqvLower(pow(mid,2),a)
        if t == 0:
            return mid
        elif t == 1:
            r = mid
        else:
            l = mid
    return mid
def log2(a):
    c = []
    k = 0
    for i in a:
        c.append(i)
    while graterEqvLower(c,[1]) == 1:
        c = delNum(c,2)
        k+=1
    return k
a = [int(s) for s in reversed(input())]
# b = [int(s) for s in reversed(input())]
# x = int(input())
print( log2(a))
# write(delNum(a,x))