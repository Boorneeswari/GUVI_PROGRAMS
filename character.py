import string
lis=list(string.ascii_lowercase+string.ascii_uppercase)
word=input()
check=word.lower()
check=check.split()
for i in check:
    if i in lis:
        print("yes")
    else:
        print("no")
