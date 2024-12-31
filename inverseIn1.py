x=input("Input :")
for i in range(len(x)):
    for j in range(i,-1,-1):
        print(x[j],end="")
    print()
