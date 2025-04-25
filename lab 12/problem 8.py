class String:
    def __init__(self, text=""):
        self.text = text

    def __iadd__(self, other):
        # Overloads += for string concatenation
        self.text += other.text if isinstance(other, String) else str(other)
        return self

    def toLower(self):
        self.text = self.text.lower()

    def toUpper(self):
        self.text = self.text.upper()

    def display(self):
        print("String:", self.text)



s1 = String("Hello")
s2 = String(" World")

print("Original Strings:")
s1.display()
s2.display()

# Concatenation using +=
s1 += s2
print("\nAfter Concatenation:")
s1.display()

# lowercase
s1.toLower()
print("\nAfter toLower():")
s1.display()

#uppercase
s1.toUpper()
print("\nAfter toUpper():")
s1.display()
