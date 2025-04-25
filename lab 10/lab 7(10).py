employee_data={
    "empcode":190098,
    "empname":"manav",
    "doj":"2025-02-15",
    "salary":80000
}

with open("employe.txt","w") as file:
    for key,value in employee_data.items():
        file.write(f"{key}:{value}\n")
    
print("employee data serialize in text file")

loaded_data={}

with open("employe.txt","r") as file:
    for line in file:
        key,value=line.strip().split(":")
        loaded_data[key]=value

loaded_data["salary"]=float(loaded_data["salary"])

print("employee data desirialize from text file")

for key,value in loaded_data.items():
    print(f"{key}:{value}")