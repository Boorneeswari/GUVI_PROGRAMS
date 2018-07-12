numb=input()
lis=[]
num=int(numb)
while(num!=0):
    rem=num%10
    lis.append(str(rem))
    num=num//10
lis1=list(numb)
if lis == lis1:
    print("yes")
else:
    print("no")
