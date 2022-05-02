def fac(n):
    if n==0: return 1
    return n*fac(n-1)
def comb(n,x):
    return fac(n)/(fac(x)*fac(n-x))
def b(n,x,p):
    return comb(n,x)*(p**x)*((1-p)**(n-x))
x,y=map(float,input().split())
p=x/(x+y)
print(round(sum([b(6,i,p) for i in range(3,7)]),3))
