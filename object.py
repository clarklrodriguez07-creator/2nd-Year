while True:    
    print("=========================")   
    print("    SIMPLE CALCULATOR")  
    print("=========================")   
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Exponentation")
    print("[6] Modulo")
    print("[7] Floor Division")
    print("[8] Exit")
    print("=========================")

    choice = int(input("\nEnter your choice: "))

    if choice == 8:
        print("Goodbye!")
        break
    elif 1 <= choice <= 7:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        

        if choice == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == 3:
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            print(f"{num1} / {num2} = {num1 / num2}")
        elif choice == 5:
            print(f"{num1} ** {num2} = {num1 ** num2}")
        elif choice == 6:
            print(f"{num1} % {num2} = {num1 % num2}")
        elif choice == 7:
            print(f"{num1} // {num2} = {num1 // num2}")

    else:
        print("Invalid choice. Please try again.")
