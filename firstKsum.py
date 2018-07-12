ran=input()
ran=ran.split()
num=int(ran[0])
upto=int(ran[1])
arr=input()
arr=arr.split()
sum=0
for i in range(0,upto):
    sum=sum+(int(arr[i]))
print(sum)
