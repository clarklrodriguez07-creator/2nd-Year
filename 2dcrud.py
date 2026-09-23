branch = int(input("Enter Number of branch: "))
customer = int(input("Enter Number of Customers: "))
print()
loan = []

while True:
    print("Menu \n1. Add \n2. Search \n3. Update \n4. Delete \n5. Display \n6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(branch):
            sample = []
            print(f"\nBranch {i + 1}")
            for j in range(customer):
                print(f"Customer {j + 1}")
                amount = float(input("Enter Loan Amount: "))
                term = int(input("Loan Term (in years): "))

                if amount >= 500000:
                    rate = 0.05
                elif 300000 <= amount <= 499999:
                    rate = 0.06
                elif 100000 <= amount <= 299999:
                    rate = 0.07
                else:
                    rate = 0.08

                interest = amount * rate * term
                totalpayment = amount + interest

                result = [amount, term, interest, totalpayment]
            sample.append(result)
        loan.append(sample) 

    elif choice == 2:       
        search1 = float(input("\nSearch Loan Amount: "))
        search2 = int(input("Search Term Years: "))
        found = False
        for i in range(branch):
            for j in range(len(loan[i])):
                if loan[i][j][0] == search1:
                    if loan[i][j][1] == search2:
                        print(f"Loan Amount: {loan[i][j][0]}")
                        print(f"Interest Amount: {loan[i][j][2]}")
                        print(f"Total Payment: {loan[i][j][3]}")
                        found = True
                        break
        if found == False:
            print("\nNot found.")

    elif choice == 3:
        update1 = float(input("\nUpdate Loan: "))
        update2 = int(input("Update Year: "))
        found = False
        for i in range(branch):
            for j in range(len(loan[i])):
                if loan[i][j][0] == update1:
                    if loan[i][j][1] == update2:
                        new_amount = float(input("\nEnter New Loan Amount: "))
                        new_term = int(input("Enter New Loan Term (in years): "))

                        if new_amount >= 500000:
                            new_rate = 0.05
                        elif 300000 <= new_amount <= 499999:
                            new_rate = 0.06
                        elif 100000 <= new_amount <= 299999:
                            new_rate = 0.07
                        else:
                            new_rate = 0.08

                        new_interest = new_amount * new_rate * new_term
                        new_totalpayment = new_amount + new_interest

                        updated_result = [new_amount, new_term, new_interest, new_totalpayment]
                        loan[i][j] = updated_result
                        print("\nLoan details updated successfully!")
                        found = True
                        break
        if found == False:
            print("\nNot found.")   

    elif choice == 4:    
        delete1 = float(input("\nDelete Loan: "))
        delete2 = int(input("Delete Term (in years): "))
        found = False
        for i in range(branch):
            for j in range(len(loan[i])):
                if loan[i][j][0] == delete1:
                    if loan[i][j][1] == delete2:
                        del loan[i][j]
                        print("\nLoan details deleted successfully!")
                        found = True
                        break
        if found == False:
            print("Not Found.")

    elif choice == 5:
        for i in range(branch):
            print(f"\nBranch {i + 1}")
            for j in range(len(loan[i])):
                print(f"Customer {j + 1}")
                print(f"Loan Amount: {loan[i][j][0]}")
                
    elif choice == 6:
        print("Exiting the program.")
        break
    else:
        print("That is not a valid choice. Please try again.")

#GOODLUCK TOMMOROW ASSESSMENT MYSELF
#error noo :(()