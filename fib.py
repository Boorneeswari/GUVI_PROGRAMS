num=int(input())
x=0
y=-1
z=1
lis=[]
for i in range(0,num+1):
    x=y+z
    y=z
    z=x
    lis.append(x)
lis=lis[1:]
for i in lis:
    print i,
