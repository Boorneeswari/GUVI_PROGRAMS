num=raw_input()
num=num.split()
N=int(num[0])
A=int(num[1])
D=int(num[2])
last=A+(N-1)*D
sum=N*(A+last)/2
print(sum)
