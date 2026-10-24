"""Electricity billing system using parallel one-dimensional arrays."""

meter_numbers = []
present_readings = []
previous_readings = []
register_types = []
consumptions = []
electricity_rates = []
principals = []
service_charges = []
vats = []
amounts_payable = []


def find_meter(meter_number):
	for index, number in enumerate(meter_numbers):
		if number == meter_number:
			return index
	return -1


def calculate_bill(present, previous, register_type):
	consumption = present - previous
	if consumption < 0:
		raise ValueError("Present reading cannot be less than previous reading.")

	if consumption < 75:
		rate = 2.50
	elif consumption <= 150:
		rate = 3.50
	elif consumption <= 200:
		rate = 4.50
	else:
		# Continue the stated pattern: the rate increases by $1 per 50 units.
		rate = 5.50 + (int(consumption - 201) // 50)

	principal = consumption * rate
	service = 30.00 if register_type == "home" else 50.00
	vat = principal * 0.10
	payable = principal + service + vat
	return consumption, rate, principal, service, vat, payable


def insert_record():
	meter_number = input("Meter number: ").strip()
	if find_meter(meter_number) != -1:
		print("That meter number already exists.")
		return

	try:
		present = float(input("Present reading: "))
		previous = float(input("Previous reading: "))
		register_type = input("Register type (home/business): ").strip().lower()
		if register_type not in ("home", "business"):
			print("Register type must be home or business.")
			return
		bill = calculate_bill(present, previous, register_type)
	except ValueError as error:
		print(f"Invalid input: {error}")
		return

	meter_numbers.append(meter_number)
	present_readings.append(present)
	previous_readings.append(previous)
	register_types.append(register_type)
	(consumption, rate, principal, service, vat, payable) = bill
	consumptions.append(consumption)
	electricity_rates.append(rate)
	principals.append(principal)
	service_charges.append(service)
	vats.append(vat)
	amounts_payable.append(payable)
	print("Record inserted.")


def display_record(index):
	print(f"Meter number:      {meter_numbers[index]}")
	print(f"Present reading:   {present_readings[index]:.2f}")
	print(f"Previous reading:  {previous_readings[index]:.2f}")
	print(f"Register type:     {register_types[index]}")
	print(f"Consumption:       {consumptions[index]:.2f}")
	print(f"Electricity rate:  ${electricity_rates[index]:.2f} per unit")
	print(f"Principal:         ${principals[index]:.2f}")
	print(f"Service charge:    ${service_charges[index]:.2f}")
	print(f"VAT (10%):         ${vats[index]:.2f}")
	print(f"Amount payable:    ${amounts_payable[index]:.2f}")


def search_record():
	meter_number = input("Meter number to search: ").strip()
	index = find_meter(meter_number)
	if index == -1:
		print("Meter not found.")
	else:
		display_record(index)


def update_record():
	meter_number = input("Meter number to update: ").strip()
	index = find_meter(meter_number)
	if index == -1:
		print("Meter not found.")
		return

	try:
		present = float(input("New present reading: "))
		previous = float(input("New previous reading: "))
		register_type = input("New register type (home/business): ").strip().lower()
		if register_type not in ("home", "business"):
			print("Register type must be home or business.")
			return
		bill = calculate_bill(present, previous, register_type)
	except ValueError as error:
		print(f"Invalid input: {error}")
		return

	present_readings[index] = present
	previous_readings[index] = previous
	register_types[index] = register_type
	(consumptions[index], electricity_rates[index], principals[index],
	 service_charges[index], vats[index], amounts_payable[index]) = bill
	print("Record updated.")


def display_all():
	if not meter_numbers:
		print("No electricity records.")
		return
	for index in range(len(meter_numbers)):
		print(f"\n--- Record {index + 1} ---")
		display_record(index)


def main():
	actions = {"1": insert_record, "2": search_record,
			   "3": update_record, "4": display_all}
	while True:
		print("\nElectricity Billing System")
		print("1. Insert  2. Search  3. Update  4. Display all  5. Exit")
		choice = input("Select an option: ").strip()
		if choice == "5":
			break
		action = actions.get(choice)
		if action:
			action()
		else:
			print("Please select a valid option.")


if __name__ == "__main__":
	main()
#secret