k = 1
bill = [3, 10, 2, 9]
b = 12

# Calculates the price Anna should pay
bill.remove(bill[k])
charged = sum(bill) / 2

# Check if Brian calculates correctly and return the difference if wrong
if b > charged:
    print(int(str(b - charged).replace('.0','')))
elif b <= charged:
    print("Bon Appetit")
