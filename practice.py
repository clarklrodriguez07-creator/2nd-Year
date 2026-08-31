from array import *

responder_names = ['Juan Cruz', 'Maria Santos', 'Pedro Reyes', 'Ana Garcia', 'Leo Mendoza']
contact_numbers = ["09171234567", "09184567890", "09981234567", "09351234567", "09271234567"]

for i in range(5):
    name = input("Enter responder name: ")
    number = input("Enter contact number: ")
    responder_names.append(name)
    contact_numbers.append(number)

print("\nEmergency Contact Directory")

for i in range(len(responder_names)):
    print(f"Responder Name: {responder_names[i]}, Contact Number: {contact_numbers[i]}")

search = input("Enter responder name to search: ")

found = False

for i in range(len(responder_names)):
    if responder_names[i].lower() == search.lower():
         print(f"Contact Number for {responder_names[i]}: {contact_numbers[i]}")
         found = True

if found == False:
    print("Responder not found.")