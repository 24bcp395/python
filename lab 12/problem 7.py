class Weather:
    def __init__(self, conditions):
        self.conditions = conditions  # list of weather conditions

    def __contains__(self, item):
        return item in self.conditions  # overloads the 'in' operator

    def display(self):
        print("Weather conditions:", self.conditions)



today = Weather(["Sunny", "Humid", "Windy"])

today.display()

print("\nIs 'Rainy' in today's weather?", 'Rainy' in today)  
print("Is 'Sunny' in today's weather?", 'Sunny' in today)     
