l=[44,62,33,99,88]
for i in range(len(l)):
    for j in range(len(l)):
        if(l[i]>l[j]):
            temp=l[j]
            l[j]=l[i]
            l[i]=temp
print(l[1])
