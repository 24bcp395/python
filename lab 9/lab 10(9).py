def frequency():
    string=input("enter string here:")
    words=string.lower().split()
    count={}
    
    for word in words:
        word=word.strip(".,!#@(){}[];:")
        count[word]=count.get(word,0)+1
    dict(sorted(count.items()))
    print(count)
    
frequency()    
    