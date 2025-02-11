string1=input("enter a string here:")
string2=input("enter another string:")
new_string=""
if string2 in string1:
    new_string=string1.replace(string2,'')

print(new_string)
