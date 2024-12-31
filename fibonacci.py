
def fibo(x):
    if x==1:
        return 1
    elif x==2:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

if __name__=="__main__":
    x=int(input("input:"))
    print(fibo(x))
