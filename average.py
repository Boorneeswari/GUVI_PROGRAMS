inp=int(input())
num=raw_input()
num=num.split()
lis=[]
for i in range(inp):
    lis.append(int(num[i]))
summ=sum(lis)
avg=summ//len(lis)
print(avg)
