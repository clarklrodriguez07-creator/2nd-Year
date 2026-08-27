from array import *

company = array('i', [])
commision = array('f', [])

size = int(input("Enter Size: "))
for i in range(size):
    sales = int(input("Enter Sales: "))
    company.append(sales)

for i in range(size):
    if company[i] >= 100000:
        commision.append(company[i] * 0.10)
    elif company[i] >= 50000:
        commision.append(company[i] * 0.07)
    elif company[i] >= 20000:
        commision.append(company[i] * 0.05)
    else:
        commision.append(company[i] * 0.02)

for i in range(size):
    print(f"\nSales: {company[i]} Commission: {commision[i]}")        

s = int(input("\nEnter number to search: "))

for i in range(size):
    if s == company[i]:
        print(f"Index found at {i}")
        break
else:
    print("Index not found.")