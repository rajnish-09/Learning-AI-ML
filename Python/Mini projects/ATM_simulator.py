# Program to simulate ATM functionality (withdraw, depost and check balance)

current_balance = 50000
user_input = input("Enter\n1. To withdraw \n2. To deposit \n3. To check balance\n")
if user_input == '1':
    withdraw_amount = int(input("Enter the amount you want to withdraw: "))
    if withdraw_amount > current_balance:
        print("Insuffient balance. Please try again.")
    elif withdraw_amount < 0:
        print("Invalid amount.")
    else:
        current_balance = current_balance - withdraw_amount
        print(f"{withdraw_amount} amount withdrawn successfully.")
        print(f'Remaining balance: {current_balance}')
elif user_input == '2':
    deposit_amount = int(input("Enter deposit amount: "))
    current_balance += deposit_amount
    print(f'Successfully deposited.\nCurrent balance: {current_balance}')
elif user_input == '3':
    print(f"Current balance: {current_balance}")
else:
    print("Invalid")
