"""Tests for Bank class."""
import unittest
from bank import Bank
from account import Account


class TestBank(unittest.TestCase):
    """Test cases for Bank class."""
    
    def setUp(self):
        """Set up test bank."""
        self.bank = Bank("Test Bank")
    
    def test_create_bank(self):
        """Test bank creation."""
        self.assertEqual(self.bank.name, "Test Bank")
        self.assertEqual(len(self.bank.accounts), 0)
    
    def test_create_account(self):
        """Test creating an account through bank."""
        account = self.bank.create_account("John Doe", 1000.0)
        self.assertIsInstance(account, Account)
        self.assertEqual(account.customer_name, "John Doe")
        self.assertEqual(account.balance, 1000.0)
        self.assertEqual(len(self.bank.accounts), 1)
    
    def test_create_multiple_accounts(self):
        """Test creating multiple accounts."""
        account1 = self.bank.create_account("Alice", 500.0)
        account2 = self.bank.create_account("Bob", 1000.0)
        
        self.assertEqual(len(self.bank.accounts), 2)
        self.assertNotEqual(account1.account_number, account2.account_number)
    
    def test_get_account(self):
        """Test getting an account by number."""
        account = self.bank.create_account("Charlie", 750.0)
        retrieved = self.bank.get_account(account.account_number)
        
        self.assertEqual(retrieved, account)
        self.assertEqual(retrieved.customer_name, "Charlie")
    
    def test_get_nonexistent_account(self):
        """Test getting a non-existent account."""
        account = self.bank.get_account("9999")
        self.assertIsNone(account)
    
    def test_list_accounts(self):
        """Test listing all accounts."""
        self.bank.create_account("David", 100.0)
        self.bank.create_account("Emma", 200.0)
        self.bank.create_account("Frank", 300.0)
        
        accounts = self.bank.list_accounts()
        self.assertEqual(len(accounts), 3)
    
    def test_transfer(self):
        """Test transferring money between accounts."""
        account1 = self.bank.create_account("Grace", 1000.0)
        account2 = self.bank.create_account("Henry", 500.0)
        
        self.bank.transfer(account1.account_number, account2.account_number, 300.0)
        
        self.assertEqual(account1.balance, 700.0)
        self.assertEqual(account2.balance, 800.0)
    
    def test_transfer_insufficient_funds(self):
        """Test transfer with insufficient funds."""
        account1 = self.bank.create_account("Ivy", 100.0)
        account2 = self.bank.create_account("Jack", 500.0)
        
        with self.assertRaises(ValueError):
            self.bank.transfer(account1.account_number, account2.account_number, 200.0)
    
    def test_transfer_invalid_source(self):
        """Test transfer with invalid source account."""
        account2 = self.bank.create_account("Kate", 500.0)
        
        with self.assertRaises(ValueError):
            self.bank.transfer("9999", account2.account_number, 100.0)
    
    def test_transfer_invalid_destination(self):
        """Test transfer with invalid destination account."""
        account1 = self.bank.create_account("Leo", 500.0)
        
        with self.assertRaises(ValueError):
            self.bank.transfer(account1.account_number, "9999", 100.0)
    
    def test_transfer_negative_amount(self):
        """Test transfer with negative amount."""
        account1 = self.bank.create_account("Mike", 1000.0)
        account2 = self.bank.create_account("Nina", 500.0)
        
        with self.assertRaises(ValueError):
            self.bank.transfer(account1.account_number, account2.account_number, -100.0)
    
    def test_get_total_deposits(self):
        """Test getting total deposits."""
        self.bank.create_account("Oscar", 1000.0)
        self.bank.create_account("Paula", 2000.0)
        self.bank.create_account("Quinn", 1500.0)
        
        total = self.bank.get_total_deposits()
        self.assertEqual(total, 4500.0)


if __name__ == '__main__':
    unittest.main()
