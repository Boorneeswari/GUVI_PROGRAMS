inp1=raw_input()
inp1=inp1.split(" ")
li=list(inp1)
lis=[]
for i in range(0,9):
    lis.append(int(li[i]))
print(min(lis))
