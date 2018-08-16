inp=int(input())
num=raw_input()
num=num.split()
lis=[]
for i in range(inp):
    lis.append(int(num[i]))
print min(lis),max(lis)
