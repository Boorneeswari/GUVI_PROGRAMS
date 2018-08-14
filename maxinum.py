num=raw_input()
num=num.split()
lis=[]
for i in range(0,10):
    lis.append(int(num[i]))
print(max(lis))
