numb1=input()
try:
    i = int(numb1) #if any string entered throws error
except ValueError:
    print ('Zero')
else:
    if int(numb1)>0:
        print("Positive")
    elif int(numb1)==0:
        print("Zero")
    else:
        print("Negative")
