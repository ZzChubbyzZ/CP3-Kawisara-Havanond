totalPrice = int(input("Price(THB) : "))
def vatcalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatcalculate(totalPrice))