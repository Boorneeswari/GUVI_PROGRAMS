num=input()
num=num.split()
frst=int(num[0])
sec=int(num[1])
c=0
lis=[]
lis1=[]
summ=0
for i in range(frst,sec):
  lis.append(i)
for i in lis:
  while(i>0):
    rem=i%10
    x=(rem*rem*rem)
    i=i//10
    summ=summ+x
  lis1.append(summ)
  summ=0
for j in lis1:
  if j in lis:
    if lis.index(j)==lis1.index(j):
      print(j)
  else:
    pass
  
