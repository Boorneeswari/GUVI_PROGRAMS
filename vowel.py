
lis=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowel=['a','e','i','o','u']
word=input()
check=word.lower()

for i in check:
    if i in vowel:
        print("Vowel")
    elif i in lis:
        print("Consonant")
    else:
        print("invalid")

