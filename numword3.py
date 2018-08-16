lisword=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
lisnum=[1,2,3,4,5,6,7,8,9,10]
inp=int(input())
if inp in lisnum:
    ind=lisnum.index(inp)
    print(lisword[ind])
