num=raw_input()
count=0
for i in num:
    if i.isdigit()==True or i.isalpha()==True:
        pass
    else:
        count=count+1
print(count)
