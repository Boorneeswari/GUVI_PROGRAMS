sizee=int(input())
list1=[]
num1=raw_input()
num1=num1.split()
for i in range(sizee):
  list1.append(int(num1[i]))
list1.sort()
for i in list1:
  print i,
