lis=[]
for i in range(1,11):
    lis.append(i*10)
inp=int(input())
for i in range(len(lis)):
    if inp <= lis[i]:
        print lis[i]
        break
