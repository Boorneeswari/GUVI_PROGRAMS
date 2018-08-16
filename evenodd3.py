inp=raw_input()
inp=inp.split()
frst=int(inp[0])
sec=int(inp[1])
prod=frst*sec
if prod%2==0:
    print("even")
else:
    print("odd")
