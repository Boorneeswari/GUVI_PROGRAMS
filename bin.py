inp1=raw_input()
lis=['0','1']
cnt=0
cnt1=0
lis1=list(inp1)
for i in range (len(lis1)):
    if lis1[i] in lis:
        cnt=cnt+1
        if cnt==len(lis1):
            print("yes")
    else:
        print("no")
        break
