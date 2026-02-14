"""Bank module for managing multiple accounts."""
from typing import Dict, Optional, List
from account import Account


class Bank:
    """Represents a bank that manages multiple accounts."""
    
    def __init__(self, name: str):
        """
        Initialize a new bank.
        
        Args:
            name: Name of the bank
        """
        self.name = name
        self.accounts: Dict[str, Account] = {}
        self._next_account_number = 1000
    
    def create_account(self, customer_name: str, initial_balance: float = 0.0) -> Account:
        """
        Create a new account.
        
        Args:
            customer_name: Name of the account holder
            initial_balance: Starting balance (default: 0.0)
            
        Returns:
            The newly created Account object
        """
        account_number = self._generate_account_number()
        account = Account(account_number, customer_name, initial_balance)
        self.accounts[account_number] = account
        return account
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """
        Get an account by account number.
        
        Args:
            account_number: The account number to look up
            
        Returns:
            Account object if found, None otherwise
        """
        return self.accounts.get(account_number)
    
    def list_accounts(self) -> List[Account]:
        """Get list of all accounts."""
        return list(self.accounts.values())
    
    def transfer(self, from_account_number: str, to_account_number: str, amount: float) -> bool:
        """
        Transfer money between accounts.
        
        Args:
            from_account_number: Source account number
            to_account_number: Destination account number
            amount: Amount to transfer
            
        Returns:
            True on success
            
        Raises:
            ValueError: If amount is not positive, accounts don't exist, or insufficient funds
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        
        if not from_account:
            raise ValueError(f"Source account {from_account_number} not found")
        if not to_account:
            raise ValueError(f"Destination account {to_account_number} not found")
        
        # Ensure transactional integrity
        try:
            from_account.withdraw(amount, f"Transfer to {to_account_number}")
            try:
                to_account.deposit(amount, f"Transfer from {from_account_number}")
            except Exception as e:
                # Rollback withdrawal if deposit fails
                from_account.deposit(amount, f"Transfer rollback to {to_account_number}")
                raise ValueError(f"Transfer failed and was rolled back: {str(e)}")
        except ValueError:
            # Re-raise withdrawal errors (insufficient funds, etc.)
            raise
        
        return True
    
    def get_total_deposits(self) -> float:
        """Get total deposits across all accounts."""
        return sum(account.get_balance() for account in self.accounts.values())
    
    def _generate_account_number(self) -> str:
        """Generate a unique account number."""
        account_number = str(self._next_account_number)
        self._next_account_number += 1
        return account_number
    
    def __str__(self) -> str:
        """String representation of bank."""
        return f"Bank({self.name}, Accounts: {len(self.accounts)}, Total Deposits: ${self.get_total_deposits():.2f})"
