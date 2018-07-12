lis=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word=input()
check=word.lower()
for i in check:
    if i in lis:
        print("Alphabet")
    else:
        print("No")
