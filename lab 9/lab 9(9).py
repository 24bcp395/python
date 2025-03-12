def count_alpha_digits():
    string=input("enter a string here:")
    dic={"alphabets":0,"digits":0}
    for char in string:
        if char.isalpha():
            dic["alphabets"]+=1
        
        elif char.isdigit():
            dic["digits"]+=1
    print(dic)
count_alpha_digits()