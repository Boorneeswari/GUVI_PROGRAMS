import statistics
siz=int(input())
lis=[]
num=input()
num=num.split()
for i in range(siz):
  lis.append(int(num[i]))
print(statistics.median(lis))
