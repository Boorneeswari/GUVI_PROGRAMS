inp=input()
inp=inp.split(" ")
lis=[]
for i in inp:
    lis.append(len(i))
print(sum(lis))
