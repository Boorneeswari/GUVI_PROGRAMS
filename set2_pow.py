arr=input()
arr=arr.split()
num=int(arr[0])
lim=int(arr[1])
mul=1
for i in range(1,lim+1):
    mul=mul*num
print(mul)
    
