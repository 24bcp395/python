def convert():
    string=input("enter a string here:")
    words=set(string.split())

    sort=sorted(words)

    b=" ".join(sort)

    print("new string:",b)

convert()
