
data = [
    ["Name", "Age", "City"],
    ["manav", 21, "Rajkot"],
    ["Ujash", 20, "Junagadh"],
    ["jenil", 20, "Mumbai"]
]

# Create and write to CSV file manually
with open("people.csv", "w", newline="") as file:
    for row in data:
        line = ",".join(map(str, row))  # Convert each item to string and join with commas
        file.write(line + "\n")

print("CSV file 'people.csv' created without using csv.writer.")
