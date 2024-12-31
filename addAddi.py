def add5(x,y,*args,**kargs):
    print("local variables",locals())
    sum=sumj=0
    sum=x+y
    for i in args:
        sum+=i
    for k,j in kargs:
        sumj+=int(j)
    return sum + sumj

print(add5(10,20,3,4,5,k1=1,k2=2))
print(add5(10,20,*(3,4,5),**dict(k1=1,k2=2)))
print(add5(10,20))
