branch = int(input("Enter Number of branch: "))
customer = int(input("Enter Number of Customers: "))

loan = []

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
        rate = rate * 100

        result = [amount, term, rate, interest, totalpayment]
        sample.append(result)
    loan.append(sample)

for i in range(branch):
    print(f"\nBranch {i + 1}")
    for j in range(len(loan[i])):
        print(f"Customer {j + 1}")
        print(f"Loan Amount: {loan[i][j][0]}")
        print(f"Loan Term: {loan[i][j][1]} years")
        print(f"Interest Rate: {loan[i][j][2]}%")
        print(f"Interest Amount: {loan[i][j][3]}")
        print(f"Total Payment: {loan[i][j][4]}")       

search1 = int(input("\nSearch Branch Number: "))
search2 = int(input("Search Customer Number: "))

if search1 <= branch:
    if search2 <= customer:
        search = loan[search1 - 1][search2 - 1]

        print(f"\nLoan Amount: {search[0]}")
        print(f"Loan Term: {search[1]} years")
        print(f"Interest Rate: {search[2]}%")
        print(f"Interest Amount: {search[3]}")
        print(f"Total Payment: {search[4]}")
    else:
        print("Customer not found.")
else:
    print("Branch not found.")

update1 = int(input("\nUpdate Branch Number: "))
update2 = int(input("Update Customer Number: "))

if update1 <= branch:
    if update2 <= customer:
        update = loan[update1 - 1][update2 - 1]

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
        new_rate = new_rate * 100

        updated_result = [new_amount, new_term, new_rate, new_interest, new_totalpayment]
        loan[update1 - 1][update2 - 1] = updated_result

        print("\nLoan details updated successfully!")
    else:
        print("Customer not found.")
else:
    print("Branch not found.")

for i in range(branch):
    print(f"\nBranch {i + 1}")
    for j in range(len(loan[i])):
        print(f"Customer {j + 1}")
        print(f"Loan Amount: {loan[i][j][0]}")
        print(f"Loan Term: {loan[i][j][1]} years")
        print(f"Interest Rate: {loan[i][j][2]}%")
        print(f"Interest Amount: {loan[i][j][3]}")
        print(f"Total Payment: {loan[i][j][4]}")        

delete1 = int(input("\nDelete Branch Number: "))
delete2 = int(input("Delete Customer Number: "))

if delete1 <= branch:
    if delete2 <= customer:
        del loan[delete1 - 1][delete2 - 1]
        print("\nLoan details deleted successfully!")
    else:
        print("Customer not found.")
else:
    print("Branch not found.")

for i in range(branch):
    print(f"\nBranch {i + 1}")
    for j in range(len(loan[i])):
        print(f"Customer {j + 1}")
        print(f"Loan Amount: {loan[i][j][0]}")
        print(f"Loan Term: {loan[i][j][1]} years")
        print(f"Interest Rate: {loan[i][j][2]}%")
        print(f"Interest Amount: {loan[i][j][3]}")
        print(f"Total Payment: {loan[i][j][4]}")