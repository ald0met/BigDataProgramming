import random
K=[]
def check(n):
    K.append(n)
    primeChk=True
    for i in range(2,n):
        if n%i==0:
            primeChk=False
    if primeChk==True:
        return True
    else:
        return False


        
while True:
    m=random.randint(2,100)
    if m in K:
        break
    else:
        check(m)
        if check(m)==True:
            print("%d is prime number"%m)
        else:
            print("%d is not prime number"%m)
