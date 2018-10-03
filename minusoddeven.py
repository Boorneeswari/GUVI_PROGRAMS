inp=raw_input()
inp=inp.split()
frst=int(inp[0])
sec=int(inp[1])
minus=frst-sec
if minus%2==0:
    print("even")
else:
    print("odd")
