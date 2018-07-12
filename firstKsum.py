num=int(input())
upto=int(input())
arr=raw_input()
arr=arr.split()
sum=0
for i in range(0,upto):
    sum=sum+(int(arr[i]))
print(sum)
