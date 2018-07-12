num=raw_input()
num=num.split()
frst=int(num[0])
scnd=int(num[1])
for numb in range(frst,scnd+1):
    if numb>1:
        for i in range(2,numb):
            if numb%i==0:
                break
        else:
            print numb,
