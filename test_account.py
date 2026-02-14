"""Tests for Account class."""
import unittest
from account import Account


class TestAccount(unittest.TestCase):
    """Test cases for Account class."""
    
    def test_create_account(self):
        """Test account creation."""
        account = Account("1001", "John Doe", 1000.0)
        self.assertEqual(account.account_number, "1001")
        self.assertEqual(account.customer_name, "John Doe")
        self.assertEqual(account.balance, 1000.0)
    
    def test_create_account_with_zero_balance(self):
        """Test account creation with zero balance."""
        account = Account("1002", "Jane Smith", 0.0)
        self.assertEqual(account.balance, 0.0)
    
    def test_create_account_negative_balance(self):
        """Test that negative initial balance raises error."""
        with self.assertRaises(ValueError):
            Account("1003", "Bob Johnson", -100.0)
    
    def test_deposit(self):
        """Test depositing money."""
        account = Account("1004", "Alice Brown", 500.0)
        account.deposit(250.0)
        self.assertEqual(account.balance, 750.0)
    
    def test_deposit_negative_amount(self):
        """Test that negative deposit raises error."""
        account = Account("1005", "Charlie Wilson", 500.0)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)
    
    def test_deposit_zero_amount(self):
        """Test that zero deposit raises error."""
        account = Account("1006", "David Lee", 500.0)
        with self.assertRaises(ValueError):
            account.deposit(0.0)
    
    def test_withdraw(self):
        """Test withdrawing money."""
        account = Account("1007", "Emma Davis", 1000.0)
        account.withdraw(300.0)
        self.assertEqual(account.balance, 700.0)
    
    def test_withdraw_insufficient_funds(self):
        """Test that withdrawing more than balance raises error."""
        account = Account("1008", "Frank Miller", 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(200.0)
    
    def test_withdraw_negative_amount(self):
        """Test that negative withdrawal raises error."""
        account = Account("1009", "Grace Taylor", 500.0)
        with self.assertRaises(ValueError):
            account.withdraw(-50.0)
    
    def test_get_balance(self):
        """Test getting balance."""
        account = Account("1010", "Henry Anderson", 1500.0)
        self.assertEqual(account.get_balance(), 1500.0)
    
    def test_transaction_history(self):
        """Test transaction history tracking."""
        account = Account("1011", "Ivy Thomas", 1000.0)
        account.deposit(500.0)
        account.withdraw(200.0)
        
        history = account.get_transaction_history()
        self.assertEqual(len(history), 3)  # Initial deposit, deposit, withdrawal
        self.assertEqual(history[0]['type'], 'deposit')
        self.assertEqual(history[1]['type'], 'deposit')
        self.assertEqual(history[2]['type'], 'withdrawal')
    
    def test_multiple_transactions(self):
        """Test multiple transactions."""
        account = Account("1012", "Jack White", 0.0)
        account.deposit(1000.0)
        account.deposit(500.0)
        account.withdraw(300.0)
        account.withdraw(200.0)
        
        self.assertEqual(account.balance, 1000.0)


if __name__ == '__main__':
    unittest.main()
