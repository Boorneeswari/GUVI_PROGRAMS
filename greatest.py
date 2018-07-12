num=raw_input()
num=num.split()
if num[0]>num[1] and num[0]>num[2]:
    print(num[0])
elif num[1]>num[2] and num[1]>num[2]:
    print(num[1])
else:
    print(num[2])

