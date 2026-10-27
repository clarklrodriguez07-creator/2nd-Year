practice = []

def add():
    while True:
        sample = []
        id = int(input("\nEnter Id: "))
        for i in range(len(practice)):
            if id == practice[i][0]:
                print("Student with this ID already exists.")
                break
        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            section = input("Enter Section: ")
            sample.append(id)
            sample.append(name)
            sample.append(age)
            sample.append(section)
            practice.append(sample)
            break

        again = input("Another Transaction?[yes/otherwise no]: ")
        if again.lower().strip() == "yes":
            continue
        else:
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

def display():
    for i in range(len(practice)):
        print(f"Student {i+1}:")
        for j in range(len(practice[i])):
            print(f"{practice[i][j]}")

def pyramid():
    n = int(input("Enter the number of rows for the pyramid: "))
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Display All Students")
    print("5. ***")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add()
    elif choice == '2':
        search()
    elif choice == '3':
        update()
    elif choice == '4':
        display()
    elif choice == '5':
        pyramid()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

#Done midterm ez project and hands on