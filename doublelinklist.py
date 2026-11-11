class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Clark:
    def __init__(self):
        self.head = None 

    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_at_position(self, index, data):
        if index < 0:
            raise IndexError("Index out of bounds.")
        if index == 0 or self.head is None:
            self.insert_front(data)
            return
        cur = self.head
        pos = 0
        while cur and pos < index:
            cur = cur.next
            pos += 1
        if cur is None:
            self.insert(data)
            return
        new_node = Node(data)
        prev_node = cur.prev
        new_node.prev = prev_node
        new_node.next = cur
        prev_node.next = new_node
        cur.prev = new_node

    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1

    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

def main():
    Empid = Clark()
    EmpName = Clark()
    HoursWorked = Clark()
    GrossIncome = Clark()
    Deduction = Clark()
    Net = Clark()

    while True:
        print("\nMenu")
        print("1. Insert at the End")
        print("2. Insert at the Beginning")
        print("3. Insert at a Specific Position")
        print("4. Display List")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            id = int(input("Enter Employee ID: "))
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

            Empid.insert(id)
            EmpName.insert(name)
            HoursWorked.insert(hours)
            GrossIncome.insert(gross)
            Deduction.insert(deduct)
            Net.insert(total)

            Empid.display() ; EmpName.display() ; HoursWorked.display() ; GrossIncome.display() ; Deduction.display() ; Net.display()       

        elif choice == 2:
            id = int(input("Enter Employee ID: "))
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

            Empid.insert_front(id)
            EmpName.insert_front(name)
            HoursWorked.insert_front(hours)
            GrossIncome.insert_front(gross)
            Deduction.insert_front(deduct)
            Net.insert_front(total)            

            Empid.display() ; EmpName.display() ; HoursWorked.display() ; GrossIncome.display() ; Deduction.display() ; Net.display()       
        
        elif choice == 3:
            target = int(input("Insert BEFORE which existing ID? "))
            pos = Empid.search(target)
            if pos == -1:
                print("Target ID not found.")
            else:
                id = int(input("Enter Employee ID: "))
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

                Empid.insert_at_position(pos, id)
                EmpName.insert_at_position(pos, name)
                HoursWorked.insert_at_position(pos, hours)
                GrossIncome.insert_at_position(pos, gross)
                Deduction.insert_at_position(pos, deduct)
                Net.insert_at_position(pos, total)

                Empid.display() ; EmpName.display() ; HoursWorked.display() ; GrossIncome.display() ; Deduction.display() ; Net.display()

        elif choice == 4:
            print("\n--- Displaying Records ---")
            print("Employee IDs:")
            Empid.display()
            print("Employee Names:")
            EmpName.display()
            print("Hours Worked:")
            HoursWorked.display()
            print("Gross Income:")
            GrossIncome.display()
            print("Deductions:")
            Deduction.display()
            print("Net Income:")
            Net.display()

        elif choice == 5:
            print("Exited Successfully.")
            break

        else:
            print("Invalid Input")

main()