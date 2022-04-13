def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
print("Select operation.")
print("1.add (+)")
print("2.subtract (-)")
print("3.multiply (x)")
print("4.divide (/)")

while True:
    
    selection = input("enter choice(1/2/3/4): ")

    
    if selection in ('1', '2', '3', '4'):
        number1 = float(input("enter 1st number: "))
        number2 = float(input("enter 2nd number: "))

        if selection == '1':
            print(number1, "+", number2, "=", add(number1, number2))

        elif selection == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif selection == '3':
            print(number1, "x", number2, "=", multiply(number1, number2))

        elif selection == '4':
            print(number1, "/", number2, "=", divide(number1, number2))
        
        next_calc = input("more calculation? (y/n): ")
        if next_calc == "no":
          break
    
    else:
        print("enter valid Input")