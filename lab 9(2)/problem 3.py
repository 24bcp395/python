def count(string):

    if string=="":
        return 0
    
    if string[0] in "AEIOUaeiou":
        return 1+count(string[1:])
    else:
        return count(string[1:])
    
text=input("enter here:")

print(count(text))