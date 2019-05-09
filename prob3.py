l=[x for x in range(1,600851475143) if 600851475143%x==0]
li=[]
for i in l:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        li.append(i)
print(li[-1])

