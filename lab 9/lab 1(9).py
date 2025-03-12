def count_lower_upper():
    count={"uppercase":0,"lowercase":0}
    a=input("enter a string here:")

    for char in a:
        if char.isupper():
            count["uppercase"]+=1
        elif char.islower():
            count["lowercase"]+=1
    print(count)

count=count_lower_upper()
            
