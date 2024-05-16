#Ask user for input, output whether it is odd or even

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid number.")
        continue

if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

