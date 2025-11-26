import sys
from alx_be_python.programming_paradigm.bank_account import BankAccount


def main():
    # We are starting with $100 in the bank for testing
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # This splits the command (e.g., "deposit:50") into parts
    command_parts = sys.argv[1].split(":")
    command = command_parts[0]

    # We check if there is an amount provided
    if len(command_parts) > 1:
        amount = float(command_parts[1])
    else:
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
