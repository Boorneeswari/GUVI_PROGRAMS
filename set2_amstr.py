num=int(input())
num1=num
c=0
while(num!=0):
    rem=num%10
    c=c+(rem*rem*rem)
    num=num//10
if num1==c:
    print("yes")
else:
    print("no")
