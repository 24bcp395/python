f=open("C:\\Users\Mac\\Documents\\python\\Book1.csv")
all_data=f.readlines()
print(all_data)
filter=[lines.strip().split(",")for lines in all_data]
print("\n",filter)

empty_dictionary={}
columns=len(filter[0])
for i in range(columns):
    empty_dictionary[filter[0][i]]=[lines[i]for lines in filter[1:]]
f.close()
print(empty_dictionary)
