
print("=== Daily Expense Calculator ===")

expenses = []
total = 0.0

count = int(input("How many expenses do you want to enter? "))

for i in range(count):
    name = input(f"Enter expense {i + 1} name: ")
    amount = float(input(f"Enter amount for {name}: "))

    expenses.append((name, amount))
    total += amount

print("\n=== Expense Summary ===")

for name, amount in expenses:
    print(f"{name}: ₹{amount:.2f}")

print("------------------------")
print(f"Total expenses: ₹{total:.2f}")

if count > 0:
    print(f"Average expense: ₹{total / count:.2f}")
