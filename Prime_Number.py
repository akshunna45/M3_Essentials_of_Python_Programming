n=int(input())
li=list()
for j in range(n):
    li.append(int(input()))
for num in li:
    m=num//2
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
            break
    if num<0:
        flag=False
    if flag:
        print("PRIME")
    else:
        print("NOT-PRIME")