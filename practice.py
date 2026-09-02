from array import array

customer_names = []
customer_ids = array('i', [])
quantities = array('i', [])
flavors = []
amounts = array('f', [])
total_amounts = array('f', [])

size = int(input("Enter number of customers: "))

while True:
    print("\n1. ADD \n2. SEARCH \n3. UPDATE \n4. DELETE \n5. DISPLAY \n6. EXIT")
    choice = int(input("\nEnter your choice: "))
    print("")
    if choice == 1:
        for i in range(size):
            customer_names.append(input("Customer name: "))
            customer_ids.append(int(input("Customer ID: ")))
            quantities.append(int(input("Quantity: ")))
            flavors.append(input("Flavor: "))
            amounts.append(float(input("Amount per item: ")))
            total_amounts.append(quantities[-1] * amounts[-1])
        print("Customer(s) added successfully.")
    elif choice == 2:
        search = int(input("Enter customer ID to search: "))
        for i in range(len(customer_ids)):
            if customer_ids[i] == search:
                print("Customer name: ", customer_names[i])
                print("Customer ID: ", customer_ids[i])
                print("Quantity: ", quantities[i])
                print("Flavor: ", flavors[i])
                print("Amount per item: ", amounts[i])
                print("Total amount: ", total_amounts[i])
                break
        else:
            print("Customer not found.")
    elif choice == 3:
        upd = int(input("Enter customer ID to update: "))
        for i in range(len(customer_ids)):
            if customer_ids[i] == upd:
                customer_names[i] = input("Customer name: ")
                quantities[i] = int(input("Quantity: "))
                flavors[i] = input("Flavor: ")
                amounts[i] = float(input("Amount per item: "))
                total_amounts[i] = quantities[i] * amounts[i]
                print("Customer updated successfully.")
                break
        else:
            print("Customer not found.")
    elif choice == 4:
        delete_id = int(input("Enter customer ID to delete: "))
        for i in range(len(customer_ids)):
            if customer_ids[i] == delete_id:
                customer_names.pop(i)
                customer_ids.pop(i)
                quantities.pop(i)
                flavors.pop(i)
                amounts.pop(i)
                total_amounts.pop(i)
                print("Customer deleted successfully.")
                break
        else:
            print("Customer not found.")
    elif choice == 5:
        if not customer_ids:
            print("No customers found.")
        for i in range(len(customer_ids)):
            print(
                f"{customer_names[i]} | ID: {customer_ids[i]} | "
                f"Quantity: {quantities[i]} | Flavor: {flavors[i]} | "
                f"Amount: {amounts[i]:.2f} | Total: {total_amounts[i]:.2f}"
            )
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")