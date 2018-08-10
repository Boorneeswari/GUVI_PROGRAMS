time=raw_input()
time1=raw_input()
time=time.split()
time1=time1.split()
hrs=abs(int(time[0])-int(time1[0]))
min=abs(int(time[1])-int(time1[1]))
print hrs,min
