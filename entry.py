print("Hello World!")

print("After this Should learn basic python skills")

if 10 > 5:
    print("10 is greater than 5")

print(3 + 7)
print(2 * 5)
print("I am", 19, "years old")

x, y, z = 10, 5, 15
print(x)
print(y)
print(z)

fruit=["apple", "banana", "cherry"]
a, b, c = fruit
print(a)   
print(b)
print(c)

print("If 10 - 5 is greater than 3")    
if 10 - 5 > 3:
    print("True")
else:
    print("None of the above")

name = input("What is your name? ")
print("Hello " +name+"!")
job = input("What do you do for a living? ")
expense_coverage = input("Does it fully cover all your expenses? (yes/no): ")
if expense_coverage == 'yes':
    print("So you have a nice job huh. Good for you.")
else:
    print("Minimum wage earner you should be ashamed of yourself. Get a better job.")

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Use a for loop to iterate through the list
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

print("Show me new code to learn after for loop and if else statement")

#to print a 2d array do this
store = []
row = int(input("Number of rows: "))
col = int(input("Number of columns: "))

for i in range(row):
    store.append([])
    for j in range(col):
        store[i].append(int(input(f"Enter value for row {i+1}, column {j+1}: ")))
