siz=int(input())
lis=[]
num=raw_input()
num=num.split()
for i in range(siz):
  lis.append(int(num[i]))
  
for j in lis:
  print j,lis.index(j)
