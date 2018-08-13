name=raw_input()
name=name.split(" ")
count=0
for j in name:
    if j.isdigit()==True:
        count=count+1
print(count)
