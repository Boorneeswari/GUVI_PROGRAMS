num=raw_input()
num=num.split()
frst=int(num[0])
sec=int(num[1])
inp=raw_input()
inp=inp.split()
lis=[]
for i in range(frst):
    lis.append(int(inp[i]))
print(lis.count(sec))
        
