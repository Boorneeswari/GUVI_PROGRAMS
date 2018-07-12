num=raw_input()
num=num.split()
frst=int(num[0])
scnd=int(num[1])
for i in range(frst+1,scnd):
    if i%2 ==0:
        print i,
    else:
        pass
