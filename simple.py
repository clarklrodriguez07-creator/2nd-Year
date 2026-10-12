rows = int(input("Enter Rows: "))
columns = int(input("Enter Columns: "))
#frth day tom
practice = []

for i in range(rows):
    sample = []
    for j in range(columns):
        id = int(input("\nEnter Id: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        section = input("Enter Section: ")
        store = [id, name, age, section]
        sample.append(store)
    practice.append(sample)

search = int(input("Search Id: "))
search2 = input("Search Name: ")

for i in range(rows):
    for j in range(columns):
        if practice[i][j][0] == search:
            if practice[i][j][1] == search2:
                print(f"Student {i+1}:")
                print(f"Id: {practice[i][j][0]}")
                print(f"Name: {practice[i][j][1]}")
                print(f"Age: {practice[i][j][2]}")
                print(f"Section: {practice[i][j][3]}")

update = int(input("Update Id: "))
update2 = input("Update Name: ")

for i in range(rows):
    for j in range(columns):
        if practice[i][j][0] == update:
            if practice[i][j][1] == update2:
                new_age = int(input("Enter New Age: "))
                new_section = input("Enter New Section: ")
                practice[i][j][2] = new_age
                practice[i][j][3] = new_section
                print("Student information updated successfully.")

for i in range(rows):
    print(f"Student {i+1}:")
    for j in range(columns):
        print(f"{practice[i][j]}")