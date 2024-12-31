sent=input("Input :")
print()
for i in range(0,len(sent)):
    for j in range(i,-1,-1):
        print(sent[j],end="")
    print()
