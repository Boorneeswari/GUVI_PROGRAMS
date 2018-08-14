num=raw_input()
num=num.split()
lis=[]
for each in num:
  n=len(each)
  lis.append(n)
#print(lis)
ind=lis.index(max(lis))
print(num[ind])
