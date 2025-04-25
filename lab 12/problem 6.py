class Date:
    def __init__(self, day, month, year):
        self.dmy = [day, month, year]  # store day, month, year in a list

    def display(self):
        print(f"{self.dmy[0]:02d}-{self.dmy[1]:02d}-{self.dmy[2]}")

    def __eq__(self, other):
        return self.dmy == other.dmy  # compare both lists directly


date1 = Date(25, 4, 2025)
date2 = Date(25, 4, 2025)
date3 = Date(1, 1, 2024)

print("Date 1:", end=" ")
date1.display()

print("Date 2:", end=" ")
date2.display()

print("Date 3:", end=" ")
date3.display()

print("\nIs Date 1 equal to Date 2?", date1 == date2) 
print("Is Date 1 equal to Date 3?", date1 == date3)   
