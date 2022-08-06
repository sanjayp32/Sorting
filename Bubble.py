def Bubble(x):
    c=0
    for i in range(len(x)-1):
        flag=False
        for j in range(len(x)-1-i):
            c=c+1
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
                flag=True
        print(f"Pass {i}:{x}")
        print("Count :",c)
        if not flag:
            break
x=list(map(int,input("Enter : ").split(",")))
Bubble(x)
print(x)