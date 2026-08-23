class Calculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2   
    
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2
    def exponentiate(self):
        return self.num1 ** self.num2
    def modulo(self):
        return self.num1 % self.num2
    def floor_divide(self):
        return self.num1 // self.num2
    

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
            print(f"{num1} + {num2} = {Calculator(num1, num2).add()}")
        elif choice == 2:
            print(f"{num1} - {num2} = {Calculator(num1, num2).subtract()}")
        elif choice == 3:
            print(f"{num1} * {num2} = {Calculator(num1, num2).multiply()}")
        elif choice == 4:
            print(f"{num1} / {num2} = {Calculator(num1, num2).divide()}")
        elif choice == 5:
            print(f"{num1} ** {num2} = {Calculator(num1, num2).exponentiate()}")
        elif choice == 6:
            print(f"{num1} % {num2} = {Calculator(num1, num2).modulo()}")
        elif choice == 7:
            print(f"{num1} // {num2} = {Calculator(num1, num2).floor_divide()   }")

    else:
        print("Invalid choice. Please try again.")
