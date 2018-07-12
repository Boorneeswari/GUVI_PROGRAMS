import string
lis=list(string.ascii_lowercase)
vowel=['a','e','i','o','u']
word=input()
check=word.lower()
check=check.split()
for i in check:
    if i in vowel:
        print("Vowel")
    elif i in lis:
        print("Consonant")
    else:
        print("invalid")

