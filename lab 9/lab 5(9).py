def ispangram():
    string="The quick brown fox jumps over the lazy dog"
    a=set(string)
    alphabets=set("abcdefghijklmnopqrstuvwxyz")
    if alphabets.issubset(a):
        print("pangram")
    else:
        print("not pangram")
   
        
ispangram()
