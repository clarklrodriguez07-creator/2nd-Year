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
        print(f"Value {key} not found.")
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

def main():
    meter = Clarkie()
    present = Clarkie()
    previous = Clarkie()
    register = Clarkie()
    principal = Clarkie()
    vat = Clarkie()
    amount = Clarkie()

    while True:
        print("\nMenu:\n1. Insert Data\n2. Search Data\n3. Exit")
        choice = int(input("Choice: "))

        if choice == 1:
            m = int(input("Enter Meter No: "))
            p = float(input("Enter Present Reading: "))
            pr = float(input("Enter Previous Reading: "))
            t = input("Enter Type of Registration: ").lower().strip()
            
            consumpt = p - pr

            if consumpt < 72:
                charge = 2.50
            elif consumpt <= 150:
                charge = 3.50
            elif consumpt <= 300:
                charge = 4.50
            elif consumpt <= 400:
                charge = 5.50
            elif consumpt <= 500:
                charge = 6
            else:
                charge = 6.50
            
            electricity = consumpt * charge

            if t == "home":
                demand = 20
                service = 5
            else:
                demand = 40
                service = 10

            princi = electricity + demand + service
            tax = 0.05 * princi
            pay = princi + tax

            meter.insert(m)
            present.insert(p)
            previous.insert(pr)
            register.insert(t)
            principal.insert(princi)
            vat.insert(tax)
            amount.insert(pay)

            print("Inserted Successfully")

        elif choice == 2:
            num = int(input("Search Meter No: "))
            meter.search(num)
            position = meter.search(num)

            if position != -1:
                corresponding_data = present.get_data(position)
                corresponding_data2 = previous.get_data(position)
                corresponding_data3 = register.get_data(position)
                corresponding_data4 = principal.get_data(position)
                corresponding_data5 = vat.get_data(position)
                corresponding_data6 = amount.get_data(position)
                if corresponding_data is not None:
                    print(f"Present Reading: {corresponding_data}")
                    print(f"Previous Reading: {corresponding_data2}")
                    print(f"Type of Registration: {corresponding_data3}")
                    print(f"Principal Amount: {corresponding_data4}")
                    print(f"VAT: {corresponding_data5}")
                    print(f"Total Amount: {corresponding_data6}")
                else:
                    print("No Corresponding data found in the other list.")

        elif choice == 3:
            print("Exited Successfully")
            break
        else:
            print("Invalid Input")

main()

#tommorow finish this no time today bcs of vacation