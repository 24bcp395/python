# Open the source file
source = open("C:\\Users\\Mac\\Documents\\python\\source.txt",'r')

# Read the content
content = source.read()

# Close the source file
source.close()

# Open (or create) the destination file
destination = open("C:\\Users\\Mac\\Documents\\python\\destination.txt", 'w')

# Write the content
destination.write(content)

# Close the destination file
destination.close()

print("File copied successfully!")