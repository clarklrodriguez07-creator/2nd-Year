from array import *

store = array('i', [])
discount = []

size = int(input("Enter size: "))

while True:
    print("\n1. ADD \n2. SEARCH \n3. UPDATE \n4. DELETE \n5. DISPLAY \n6. EXIT")
    choice = int(input("\nEnter your choice: "))
    print("")
    if choice == 1:
        for i in range(size):
            unit = int(input("Units Purchased: "))
            store.append(unit)
            discount.append(0) 

        for i in range(len(store)):
            if store[i] >= 100:
                disc = "20%"
            elif store[i] >= 50:
                disc = "15%"
            elif store[i] >= 20:
                disc = "10%"
            elif store[i] >= 10:
                disc = "5%"
            else:
                disc = "No Discount"

            discount[i] = disc
    elif choice == 2:
        search = int(input("Enter units to search: "))
        for i in range(len(store)):
            if store[i] == search:
                print("Units Purchased: ", store[i])
                print("Discount: ", discount[i])
                break
        else:
            print("Units not found.")
    elif choice == 3:
        upd = int(input("Enter unit to update: "))
        for i in range(len(store)):
            if store[i] == upd:
                new_unit = int(input("Enter new unit value: "))
                store[i] = new_unit
                if store[i] >= 100:
                    discount[i] = "20%"
                elif store[i] >= 50:
                    discount[i] = "15%"
                elif store[i] >= 20:
                    discount[i] = "10%"
                elif store[i] >= 10:
                    discount[i] = "5%"
                else:
                    discount[i] = "No Discount"
                print("Unit updated successfully.")
                break
        else:
            print("Unit not found.")
    elif choice == 4:
        del_unit = int(input("Enter unit to delete: "))
        for i in range(len(store)):
            if store[i] == del_unit:
                del store[i]
                del discount[i]
                print("Unit deleted successfully.")
                break
        else:
            print("Unit not found.")
    elif choice == 5:
        print("Units Purchased: ", store)
        print("Discount: ", discount)
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")