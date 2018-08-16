frst=input()
countd=0
countal=0
for i in frst:
    if i.isdigit()==True:
        countd=countd+1
    if i.isalpha()==True:
        countal=countal+1

    else:
        pass
print(countd,countal)
if countd>0 and countal>0:
    print("Yes")
else:
    print("No")
