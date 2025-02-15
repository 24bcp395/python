d1={"wafer":20,
    "kurkure":30,
    "bingo":15}
d2={"wafer":2,
    "kurkure":3,
    "bingo":5}
total=0
length=len(d1)
for item in d1:
    for item_prc in d2:
        if item==item_prc:
            total+=d1[item]*d2[item_prc]
            
totalw=d1["wafer"]*d2["wafer"]         #totalw is nothing but total price of wafer   
totalk=d1["kurkure"]*d2["kurkure"]
totalb=d1["bingo"]*d2["bingo"]
           
print("product :",length)
print("wafer :",totalw,"rupee")        
print("kurkure :",totalk,"rupee")
print("bingo :",totalb,"rupee")
print("total :",total,"rupee")