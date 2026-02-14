"""Account module for banking system."""
from datetime import datetime
from typing import List, Dict


class Account:
    """Represents a bank account."""
    
    def __init__(self, account_number: str, customer_name: str, initial_balance: float = 0.0):
        """
        Initialize a new account.
        
        Args:
            account_number: Unique account identifier
            customer_name: Name of the account holder
            initial_balance: Starting balance (default: 0.0)
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transactions: List[Dict] = []
        self.created_at = datetime.now()
        
        if initial_balance > 0:
            self._add_transaction("deposit", initial_balance, "Initial deposit")
    
    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            description: Transaction description
            
        Returns:
            True on success
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self._add_transaction("deposit", amount, description)
        return True
    
    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        """
        Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw
            description: Transaction description
            
        Returns:
            True on success
            
        Raises:
            ValueError: If amount is not positive or exceeds balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        self._add_transaction("withdrawal", amount, description)
        return True
    
    def get_balance(self) -> float:
        """Get current account balance."""
        return self.balance
    
    def get_transaction_history(self) -> List[Dict]:
        """Get list of all transactions."""
        return self.transactions.copy()
    
    def _add_transaction(self, transaction_type: str, amount: float, description: str):
        """Add a transaction to history."""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "description": description,
            "timestamp": datetime.now(),
            "balance_after": self.balance
        }
        self.transactions.append(transaction)
    
    def __str__(self) -> str:
        """String representation of account."""
        return f"Account({self.account_number}, {self.customer_name}, Balance: ${self.balance:.2f})"
    
    def __repr__(self) -> str:
        """Detailed representation of account."""
        return f"Account(account_number='{self.account_number}', customer_name='{self.customer_name}', balance={self.balance})"
