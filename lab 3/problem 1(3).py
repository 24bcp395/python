string=str(input("enter here:"))
vowels="aeiou"
count=0

for char in string:
    if char in vowels:
        count+=1

print(count)
