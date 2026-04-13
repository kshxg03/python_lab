
# Store customer balance in a variable. 
# Ask user for amount to withdraw. If desired amount is less than total balance display, 123 withdrawn successfully. 
# New Balance: 456 else display Insufficient balance. You only have 123 in your account


balance = 10000

withdraw = int(input("How much would you like to withdraw? Rs."))


if withdraw > balance:
    print("Insufficient balance, withdraw failed.")
else:
    balance -= withdraw
    print(f"Rs.{withdraw} amount successful, your remaining balance: Rs.{balance}.")