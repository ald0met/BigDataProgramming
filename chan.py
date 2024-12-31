
def count(x):
    d={}
    for i in range(len(x)): 
        d[x[i].lower()]=x.count(x[i])
    print(*['(%s:%d)'%(x,y) for x,y in d.items()])
    return 0

def trans(x):
    s=str()
    for i in x:
        if i.isupper() == True:
            s+=i.lower()
        else:
            s+=i.upper()
    print(s)

if __name__=="__main__":
    while 1:
        x=input("Input:")
        if x=="STOP":
            print("Bye")
            break
        else:
            count(x)
            trans(x)
