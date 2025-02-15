string=input("enter a string here:" )
frequency={}
for char in string:
    if char in frequency:    #check char is in dictionary or not
        frequency[char]+=1
    else:
        frequency[char]=1

for char, count in frequency.items():
    print(f"'{char}': {count}")
          
            