## Expense Tracker - Project 2

print("Welcome to Expense Tracker")
print("Enter your expenses one by one.")
print("Type 'done' to finish.\n")

total = 0  # accumulator variable

while True:
    user_input = input("Enter expense amount: ")

    if user_input.lower() == 'done':
        break

    try:
        expense = float(user_input)
        total = total + expense   # accumulator logic
        print("Added successfully!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

print("\nTotal Spent =", total)
print("Thank you!")
