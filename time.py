time=int(input())
if time <=60:
  print("0",time)
else:
  rem=time%60
  div=time//60
  print(div,rem)
