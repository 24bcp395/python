def create_vcard():
    name=input("enter name here:")
    mobile=input("enter mobile number:" )
    email=input("enter email here:")




    file_name=input("enter file nmae here(use .vcf):")

    with open(file_name,"a+") as vcard_file:
        vcard_file.write("BEGIN:VCARD"+"\n")
        vcard_file.write("VERSION:3.0"+"\n")
        vcard_file.write("FN:"+name+"\n")
        vcard_file.write("TEL:"+mobile+"\n")
        vcard_file.write("EMAIL:"+email+"\n")
        vcard_file.write("END:VCARD")
    print("vcard saved")
create_vcard()
