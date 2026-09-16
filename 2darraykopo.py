pizzashop = []

while True:
    print("\nPIZZA SHOP SA GWAPO")
    print("1. Add Order")
    print("2. Search Order")
    print("3. Display All Orders")
    print("4. Delete Order")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        order_id = input("Enter Order ID: ")
        name = input("Enter Customer Name: ")

        print("\nPizza Flavors")
        print("1. Cheese")
        print("2. Hawaiian")
        print("3. Pepperoni")
        flavor = int(input("Choose flavor: "))

        print("\nPizza Sizes")
        print("1. Small")
        print("2. Medium")
        print("3. Large")
        size = int(input("Choose size: "))

        quantity = int(input("Enter Quantity: "))

        if flavor == 1:
            flavor2 = "Cheese"
            if size == 1:
                size2 = "Small"
                price = 200
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15
            elif size == 2:
                size2 = "Medium"
                price = 250
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15
            else:
                size2 = "Large"
                price = 300
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15

        elif flavor == 2:
            flavor2 = "Hawaiian"

            if size == 1:
                size2 = "Small"
                price = 230
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15
            elif size == 2:
                size2 = "Medium"
                price = 280
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15
            else:
                size2 = "Large"
                price = 330
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15
        else:
            flavor2 = "Pepperoni"

            if size == 1:
                size2 = "Small"
                price = 260
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15
            elif size == 2:
                size2 = "Medium"
                price = 310
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15
            else:
                size2 = "Large"
                price = 360
                if quantity <= 2:
                    discount = 0
                elif quantity <= 4:
                    discount = 0.10
                else:
                    discount = 0.15

        price = price * quantity
        total_price = price - (price * discount)

        order = [
            order_id,
            name,
            flavor2,
            size2,
            quantity,
            total_price
        ]

        pizzashop.append(order)
        print("\nOrder added successfully!")

    elif choice == "2":
        search = input("Enter Order ID to search: ")
        for i in range(len(pizzashop)):
            if pizzashop[i][0] == search:
                print("\nOrder Found")
                print(f"Order ID: {pizzashop[i][0]}")
                print(f"Customer Name: {pizzashop[i][1]}")
                print(f"Pizza Flavor: {pizzashop[i][2]}")
                print(f"Pizza Size: {pizzashop[i][3]}")
                print(f"Quantity: {pizzashop[i][4]}")
                print(f"Total Price: {pizzashop[i][5]}")
                break
        else:
            print("\nOrder not found.")

    elif choice == "3":
            print("\n===== ALL ORDERS =====")
            for i in range(len(pizzashop)):
                print(f"\nOrder {i + 1}")
                print(f"Order ID: {pizzashop[i][0]}")
                print(f"Customer Name: {pizzashop[i][1]}")
                print(f"Pizza Flavor: {pizzashop[i][2]}")
                print(f"Pizza Size: {pizzashop[i][3]}")
                print(f"Quantity: {pizzashop[i][4]}")
                print(f"Total Price: {pizzashop[i][5]}")

    elif choice == "4":
            search = input("Enter Order ID to Delete: ")
            for i in range(len(pizzashop)):
                if pizzashop[i][0] == search:
                    del pizzashop[i][j]
                    print("\nOrder deleted successfully!")
                    
                    break
            else:
                print("\nOrder not found.")


    elif choice == "5":
        print("Thank you for using PIZZA SHOP SA GWAPO!")
        break

    else:
        print("Invalid choice. Try again.")

#to put 3 nested if
#first is
#if .....
    #if ....
        #if ...

        #then ...
    #then...
#then...
#that's it

#to append a 2d array
#pattern is example
#numbers = [] this is the 2d array initialize it
#for i in range(3): this is the first loop
    #row = [] this is the row to append to the 2d array
    #for j in range(3): this is the second loop
        #row.append(int(input("Enter number: "))) this is the input to append to the row
    #numbers.append(row) this is to append the row to the 2d array

#that is the normal loop to input one variable but what if it's multiple?
#pizzastore = []
#while True:
    # code for adding orders to pizzastore
    #name = input("Enter name: ")
    #flavor = input("Enter flavor: ")
    #size = input("Enter size: ")
    #quantity = int(input("Enter quantity: "))

    #order = [name, flavor, size, quantity]
    #pizzastore.append(order)
    #break

#that's how you use it on a 2d array