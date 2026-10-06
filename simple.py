rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))

practice = []

for i in range(rows):
    for j in range(columns):
        id = int(input("\nEnter Id: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        section = input("Enter Section: ")
        store = [id, name, age, section]
        practice.append(store)

for i in range(rows):
    print(f"Student {i+1}:")
    for j in range(columns):
        print(f"{practice[i][j]}")