siz=int(input())
lis=[]
num=input()
num=num.split()
for i in range(siz):
  lis.append(int(num[i]))
lis.sort()
for i in lis:
  print(i)
