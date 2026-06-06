# Bank App Part 3

income = float(input("Enter your income: "))
expense = float(input("Enter your expense: "))

balance = income - expense

print("\n----- Bank Account Summary -----")
print("income Amount:", income)
print("expense Amount:", expense)
print("Balance:", balance)

    #Validation part bank app 3
if income < 0:
        print("Income cannot be negative!")

elif expense < 0:
      print("Expense cannot be negative!")

else:
      balance = income - expense
print("Balance:", balance)