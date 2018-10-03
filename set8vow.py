strr=input()
vow=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(strr)):
    if strr[i] in vow:
        print("yes")
        break
else:
    print("no")
