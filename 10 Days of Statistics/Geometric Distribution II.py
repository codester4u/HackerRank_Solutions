p=1/3
def g_val(k,p):
    return p*(1-p)**(k-1)
print(round(sum([g_val(i,p) for i in range(1,6)]),3))
