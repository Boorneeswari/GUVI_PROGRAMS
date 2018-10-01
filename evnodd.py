inp1=raw_input()
inp1=inp1.split(" ")
lis=[]
for i in range(len(inp1)):
    lis.append(int(inp1[i]))
adding=sum(lis)
if adding%2==0:
    print("even")
else:
    print("odd")
