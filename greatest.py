num=raw_input()
num=num.split()
for i in range(len(num)):
    lis.append(int(num[i]))
print(max(lis))
