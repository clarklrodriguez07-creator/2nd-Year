    class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Clarkie:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        print(f"Employee ID {key} not found.")
        return -1

    def get_data(self, position):
        current = self.head
        index = 0
        while current:
            if index == position:
                return current.data
            current = current.next
            index += 1
        return None

    def update(self, position, new_value):
        current = self.head
        index = 0
        while current:
            if index == position:
                current.data = new_value
                return
            current = current.next
            index += 1
    
    def delete(self, key):
        current = self.head
        prev = None
        
        if current and current.data == key:
            self.head = current.next
            print(f"Deleted {key}")
            return

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} is not found")
            return
        
        prev.next = current.next
        print(f"Deleted {key}")

    def delete_at_position(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        index = 0
        while current and index < position -1:
            current = current.next
            index +=1
        if current and current.next:
            current.next = current.next.next

    def display(self):
        current = self.head
        if current is None:
            print("None")
            return
        while current:
            print(current.data)
            current = current.next
        print("None")


def main():
    empid = Clarkie()
    empname = Clarkie()
    hoursworked = Clarkie()
    grossincome = Clarkie()
    deduction = Clarkie()
    net = Clarkie()

    while True:
        print("\nMenu:\nA. Insert Record\nB. Search Record\nC. Update Record\nD. Display\nE. Exit")
        choice = input("\nChoose: ").upper().strip()

        if choice == "A":
            eid = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            hours = float(input("Enter Hours Worked: "))

            if hours <= 80:
                regular = hours
                overtime = 0
            else:
                regular = 80
                overtime = hours - 80

            bonus = 0
            if hours > 85:
                bonus = 1000

            regular_pay = regular * 65.5
            overtime_pay = overtime * (65.5 * 1.5)

            gross = regular_pay + overtime_pay + bonus

            if gross <= 3000:
                federal = gross * 0.10
                state = gross * 0.05
            else:
                federal = gross * 0.12
                state = gross * 0.06

            social = gross * 0.062
            medicare = gross * 0.0145
            insurance = 400

            deduct = federal + state + social + medicare + insurance
            total = gross - deduct

            empid.insert(eid)
            empname.insert(name)
            hoursworked.insert(hours)
            grossincome.insert(gross)
            deduction.insert(deduct)
            net.insert(total)

            print("\n--- Inserted Record ---")
            print(f"EmpId: {eid}")
            print(f"EmpName: {name}")
            print(f"HoursWorked: {hours}")
            print(f"GrossIncome: {gross:.2f}")
            print(f"Deduction: {deduct:.2f}")
            print(f"Net: {total:.2f}")
            print("Inserted Successfully")

        elif choice == "B":
            num = int(input("Search Employee ID: "))
            position = empid.search(num)

            if position != -1:
                print("\n--- Search Record ---")
                print(f"EmpId: {empid.get_data(position)}")
                print(f"EmpName: {empname.get_data(position)}")
                print(f"HoursWorked: {hoursworked.get_data(position)}")
                print(f"GrossIncome: {grossincome.get_data(position):.2f}")
                print(f"Deduction: {deduction.get_data(position):.2f}")
                print(f"Net: {net.get_data(position):.2f}")
                print("None")

        elif choice == "C":
            num = int(input("Enter Employee ID to update: "))
            position = empid.search(num)

            if position != -1:
                name = input("Enter New Employee Name: ")
                hours = float(input("Enter New Hours Worked: "))

                if hours <= 80:
                    regular = hours
                    overtime = 0
                else:
                    regular = 80
                    overtime = hours - 80

                bonus = 0
                if hours > 85:
                    bonus = 1000

                regular_pay = regular * 65.5
                overtime_pay = overtime * (65.5 * 1.5)

                gross = regular_pay + overtime_pay + bonus

                if gross <= 3000:
                    federal = gross * 0.10
                    state = gross * 0.05
                else:
                    federal = gross * 0.12
                    state = gross * 0.06

                social = gross * 0.062
                medicare = gross * 0.0145
                insurance = 400

                deduct = federal + state + social + medicare + insurance
                total = gross - deduct

                empname.update(position, name)
                hoursworked.update(position, hours)
                grossincome.update(position, gross)
                deduction.update(position, deduct)
                net.update(position, total)

                print("\n--- Displaying All Updated Records ---")

                current = empid.head
                position = 0

                while current:
                    print(f"\nEmpId: {empid.get_data(position)}")
                    print(f"EmpName: {empname.get_data(position)}")
                    print(f"HoursWorked: {hoursworked.get_data(position)}")
                    print(f"GrossIncome: {grossincome.get_data(position):.2f}")
                    print(f"Deduction: {deduction.get_data(position):.2f}")
                    print(f"Net: {net.get_data(position):.2f}")

                    current = current.next
                    position += 1
                print("None")

        elif choice == "D":
            print("\n--- Displaying All Records ---")

            current = empid.head
            position = 0

            if current is None:
                print("None")
            else:
                while current:
                    print(f"\nEmpId: {empid.get_data(position)}")
                    print(f"EmpName: {empname.get_data(position)}")
                    print(f"HoursWorked: {hoursworked.get_data(position)}")
                    print(f"GrossIncome: {grossincome.get_data(position):.2f}")
                    print(f"Deduction: {deduction.get_data(position):.2f}")
                    print(f"Net: {net.get_data(position):.2f}")

                    current = current.next
                    position += 1

                print("None")

        elif choice == "E":
            print("Exited Successfully")
            break

        else:
            print("Invalid Input")

main()
