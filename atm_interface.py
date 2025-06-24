
from datetime import datetime

filename = "account.txt"

# Load PIN and Balance from File
try:
    with open(filename, "r") as file:
        pin_code = file.readline().strip()
        balance = float(file.readline().strip())
except FileNotFoundError:
    pin_code = "1234"
    balance = 1000.0

# PIN Verification
authenticated = False
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == pin_code:
        print("Login successful.\n")
        authenticated = True
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}\n")

if not authenticated:
    print("Too many incorrect attempts. Exiting ATM.")
else:
    transactions = []

    # ATM Functions
    def check_balance():
        print(f"\nYour current balance is: ${balance:.2f}")

    def deposit_money():
        global balance
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transactions.append(f"{now} - Deposited ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw_money():
        global balance
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transactions.append(f"{now} - Withdrew ${amount}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")

    def change_pin():
        global pin_code
        current = input("Enter your current PIN: ")
        if current == pin_code:
            new_pin = input("Enter new 4-digit PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
                pin_code = new_pin
                print("PIN changed successfully.")
            else:
                print("PINs do not match or invalid format.")
        else:
            print("Incorrect current PIN.")

    def view_transaction_history():
        if not transactions:
            print("No transactions recorded yet.")
        else:
            print("\nTransaction History:")
            for t in transactions:
                print(f"- {t}")

    def save_to_file():
        with open(filename, "w") as file:
            file.write(f"{pin_code}\n")
            file.write(f"{balance}\n")

    def main_menu():
        while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("5. Change PIN")
            print("6. View Transaction History")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                check_balance()
            elif choice == "2":
                deposit_money()
            elif choice == "3":
                withdraw_money()
            elif choice == "4":
                save_to_file()
                print("Thank you for using the ATM. Goodbye!")
                break
            elif choice == "5":
                change_pin()
            elif choice == "6":
                view_transaction_history()
            else:
                print("Invalid choice. Please try again.")

    main_menu()
