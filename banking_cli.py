"""Command-line interface for the banking system."""
import sys
from bank import Bank


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("BANKING SYSTEM")
    print("=" * 50)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer")
    print("6. View Transaction History")
    print("7. List All Accounts")
    print("8. Exit")
    print("=" * 50)


def main():
    """Main function to run the banking CLI."""
    bank = Bank("MyBank")
    print(f"Welcome to {bank.name}!")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        try:
            if choice == "1":
                name = input("Enter customer name: ").strip()
                initial_balance = float(input("Enter initial balance (or 0): ").strip() or "0")
                account = bank.create_account(name, initial_balance)
                print(f"\n✓ Account created successfully!")
                print(f"Account Number: {account.account_number}")
                print(f"Customer: {account.customer_name}")
                print(f"Balance: ${account.balance:.2f}")
            
            elif choice == "2":
                account_number = input("Enter account number: ").strip()
                account = bank.get_account(account_number)
                if not account:
                    print(f"\n✗ Account {account_number} not found!")
                    continue
                amount = float(input("Enter deposit amount: ").strip())
                account.deposit(amount)
                print(f"\n✓ Deposited ${amount:.2f}")
                print(f"New balance: ${account.balance:.2f}")
            
            elif choice == "3":
                account_number = input("Enter account number: ").strip()
                account = bank.get_account(account_number)
                if not account:
                    print(f"\n✗ Account {account_number} not found!")
                    continue
                amount = float(input("Enter withdrawal amount: ").strip())
                account.withdraw(amount)
                print(f"\n✓ Withdrew ${amount:.2f}")
                print(f"New balance: ${account.balance:.2f}")
            
            elif choice == "4":
                account_number = input("Enter account number: ").strip()
                account = bank.get_account(account_number)
                if not account:
                    print(f"\n✗ Account {account_number} not found!")
                    continue
                print(f"\nAccount: {account.account_number}")
                print(f"Customer: {account.customer_name}")
                print(f"Balance: ${account.balance:.2f}")
            
            elif choice == "5":
                from_account = input("Enter source account number: ").strip()
                to_account = input("Enter destination account number: ").strip()
                amount = float(input("Enter transfer amount: ").strip())
                bank.transfer(from_account, to_account, amount)
                print(f"\n✓ Transferred ${amount:.2f} from {from_account} to {to_account}")
            
            elif choice == "6":
                account_number = input("Enter account number: ").strip()
                account = bank.get_account(account_number)
                if not account:
                    print(f"\n✗ Account {account_number} not found!")
                    continue
                transactions = account.get_transaction_history()
                print(f"\nTransaction History for Account {account_number}:")
                print("-" * 80)
                for i, trans in enumerate(transactions, 1):
                    print(f"{i}. {trans['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} | "
                          f"{trans['type'].upper()}: ${trans['amount']:.2f} | "
                          f"{trans['description']} | Balance: ${trans['balance_after']:.2f}")
            
            elif choice == "7":
                accounts = bank.list_accounts()
                if not accounts:
                    print("\nNo accounts found!")
                else:
                    print(f"\nAll Accounts in {bank.name}:")
                    print("-" * 80)
                    for account in accounts:
                        print(f"Account {account.account_number}: {account.customer_name} - "
                              f"Balance: ${account.balance:.2f}")
                    print(f"\nTotal Deposits: ${bank.get_total_deposits():.2f}")
            
            elif choice == "8":
                print("\nThank you for using our banking system. Goodbye!")
                sys.exit(0)
            
            else:
                print("\n✗ Invalid choice. Please enter a number between 1 and 8.")
        
        except ValueError as e:
            print(f"\n✗ Error: {e}")
        except Exception as e:
            print(f"\n✗ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
