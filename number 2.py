fruits = ["Mango", "Apple", "Banana", "Orange", "Grapes"]

# Write to file
with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

# Read from file
print("Your favorite fruits:")
with open("fruits.txt", "r") as f:
    for line in f:
        print(line.strip())