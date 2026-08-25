emfla = 375
unit = int(input("Emergency flashlight purchased: "))

if unit <= 30:
    total = unit * emfla
    discount = total * .10
    discounted = total - discount
    if discounted > 12000:
        add = discounted * .05
        final = discounted - add
    else:
        add = 0
        final = discounted

    if final > 15000:
        vat = final * .12
    else:
        vat = final * .08

    final = final + vat       

else:
    total = unit * emfla
    discount = total * .10
    discounted = total - discount
    add = 0
    final = discounted
    vat = final * .08
    final = final + vat


print("Total:", total)
print("Discount:", discount)
print("Additional Discount:", add)
print("VAT:", vat)
print("Final Price:", final)