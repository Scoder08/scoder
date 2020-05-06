def partition(l,x):
    l = [int(i) for i in l]
    p1 = []
    p2 = []
    i = 0
    j = len(l) - 1
    while len(p1) + len(p2) < len(l):
        if l[i] > x and x >= l[j]:
            p1.append((l[j]))
            p2 = [l[i]] + p2
            i = i + 1
            j = j - 1
        else:
            if l[i] <= x and l[j] > x:
                p1.append(l[i])
                p2 = [l[j]] + p2
                i = i + 1
                j = j - 1
            elif l[j] > x:
                p2 = [l[j]] + p2
                j = j - 1
            else:
                p1.append(l[i])
                i = i + 1

    return (len(p1))
def maxi(l,x):
    a = sorted(l)
    return a[x-1]
def check(a,b):
    for i in b :
        if a > maxi(i,len(i)):
            b= b+[[a]]
        else:
            pose = partition(i,a)
            temp = [a] + i[pose:]
            b.append(temp)
    return(b)
def monotone(l):
    if len(l) == 1 :
        c = [l]
    else:
        c =  check(l[0], monotone(l[1:]))
    return c
inp=[14,6,8,9]
a = monotone(inp)
print(a)