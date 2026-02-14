# Banking System

A simple command-line banking system implemented in Python. This system allows users to create accounts, deposit and withdraw money, transfer funds between accounts, and view transaction history.

## Features

- **Account Management**: Create new bank accounts with unique account numbers
- **Deposits**: Add money to accounts
- **Withdrawals**: Remove money from accounts (with balance validation)
- **Transfers**: Transfer money between accounts
- **Transaction History**: View all transactions for an account
- **Account Listing**: View all accounts in the bank
- **Balance Inquiry**: Check account balance

## Installation

No external dependencies are required. This project uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/adeelciit786-hue/banking2.git
cd banking2
```

## Usage

### Running the CLI Application

```bash
python banking_cli.py
```

### Using the Banking System Programmatically

```python
from bank import Bank

# Create a bank
bank = Bank("MyBank")

# Create accounts
account1 = bank.create_account("John Doe", 1000.0)
account2 = bank.create_account("Jane Smith", 500.0)

# Deposit money
account1.deposit(250.0)

# Withdraw money
account1.withdraw(100.0)

# Transfer between accounts
bank.transfer(account1.account_number, account2.account_number, 200.0)

# Check balance
print(f"Balance: ${account1.get_balance():.2f}")

# View transaction history
for trans in account1.get_transaction_history():
    print(f"{trans['type']}: ${trans['amount']:.2f}")
```

## Running Tests

```bash
# Run all tests
python -m unittest discover -s . -p "test_*.py"

# Run specific test file
python test_account.py
python test_bank.py
```

## Project Structure

```
banking2/
├── account.py          # Account class implementation
├── bank.py             # Bank class implementation
├── banking_cli.py      # Command-line interface
├── test_account.py     # Tests for Account class
├── test_bank.py        # Tests for Bank class
└── README.md           # This file
```

## Classes

### Account
Represents an individual bank account with methods for deposits, withdrawals, and transaction tracking.

**Methods:**
- `deposit(amount, description)`: Deposit money
- `withdraw(amount, description)`: Withdraw money
- `get_balance()`: Get current balance
- `get_transaction_history()`: Get all transactions

### Bank
Manages multiple accounts and provides banking operations.

**Methods:**
- `create_account(customer_name, initial_balance)`: Create new account
- `get_account(account_number)`: Get account by number
- `list_accounts()`: List all accounts
- `transfer(from_account, to_account, amount)`: Transfer funds
- `get_total_deposits()`: Get total deposits across all accounts

## Error Handling

The system includes validation for:
- Negative amounts (deposits, withdrawals, transfers)
- Insufficient funds
- Invalid account numbers
- Negative initial balance

## License

MIT License
