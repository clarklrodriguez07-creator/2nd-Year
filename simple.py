practice = []

def add():
    while True:
        sample = []
        id = int(input("\nEnter Id: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        section = input("Enter Section: ")
        store = [id, name, age, section]
        sample.append(id)
        sample.append(name)
        sample.append(age)
        sample.append(section)
        practice.append(sample)
        break

def search():
    search_id = int(input("Search Id: "))
    search_name = input("Search Name: ")

    for i in range(len(practice)):
        if practice[i][0] == search_id and practice[i][1] == search_name:
            print(f"Student {i+1}:")
            print(f"Id: {practice[i][0]}")
            print(f"Name: {practice[i][1]}")
            print(f"Age: {practice[i][2]}")
            print(f"Section: {practice[i][3]}")
            return
    else:
        print("Student not found.")

def update():
    update = int(input("Update Id: "))
    update2 = input("Update Name: ")

    for i in range(len(practice)):
        if practice[i][0] == update:
            if practice[i][1] == update2:
                new_age = int(input("Enter New Age: "))
                new_section = input("Enter New Section: ")
                practice[i][2] = new_age
                practice[i][3] = new_section
                print("Student information updated successfully.")

for i in range(len(practice)):
    print(f"Student {i+1}:")
    for j in range(len(practice[i])):
        print(f"{practice[i][j]}")