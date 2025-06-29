"""
Finance Manager class for handling transactions and data persistence
"""

import json
import os
from typing import List, Dict, Any, Optional
from datetime import datetime
from collections import defaultdict
from transaction import Transaction

class FinanceManager:
    """Manages financial transactions and data persistence"""
    
    def __init__(self, data_file: str = "finance_data.json"):
        """
        Initialize the finance manager
        
        Args:
            data_file: Path to the JSON file for data storage
        """
        self.data_file = data_file
        self.transactions: List[Transaction] = []
        self.load_data()
    
    def add_transaction(self, transaction: Transaction) -> bool:
        """
        Add a new transaction
        
        Args:
            transaction: Transaction object to add
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.transactions.append(transaction)
            self.save_data()
            return True
        except Exception as e:
            print(f"Error adding transaction: {e}")
            return False
    
    def delete_transaction(self, transaction_id: str) -> bool:
        """
        Delete a transaction by ID
        
        Args:
            transaction_id: ID of the transaction to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            original_length = len(self.transactions)
            self.transactions = [t for t in self.transactions if t.transaction_id != transaction_id]
            
            if len(self.transactions) < original_length:
                self.save_data()
                return True
            return False
        except Exception as e:
            print(f"Error deleting transaction: {e}")
            return False
    
    def get_all_transactions(self) -> List[Transaction]:
        """
        Get all transactions sorted by date (newest first)
        
        Returns:
            List of all transactions
        """
        return sorted(self.transactions, key=lambda x: x.date, reverse=True)
    
    def get_transactions_by_category(self, category: str) -> List[Transaction]:
        """
        Get transactions filtered by category
        
        Args:
            category: Category to filter by
            
        Returns:
            List of transactions in the specified category
        """
        category = category.lower()
        return [t for t in self.transactions if t.category == category]
    
    def get_transactions_by_type(self, transaction_type: str) -> List[Transaction]:
        """
        Get transactions filtered by type (income/expense)
        
        Args:
            transaction_type: 'income' or 'expense'
            
        Returns:
            List of transactions of the specified type
        """
        transaction_type = transaction_type.lower()
        return [t for t in self.transactions if t.transaction_type == transaction_type]
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get financial summary
        
        Returns:
            Dictionary containing financial summary data
        """
        income_transactions = self.get_transactions_by_type('income')
        expense_transactions = self.get_transactions_by_type('expense')
        
        total_income = sum(t.amount for t in income_transactions)
        total_expenses = sum(t.amount for t in expense_transactions)
        balance = total_income - total_expenses
        
        # Group expenses by category
        expense_by_category = defaultdict(float)
        for transaction in expense_transactions:
            expense_by_category[transaction.category] += transaction.amount
        
        # Group income by category
        income_by_category = defaultdict(float)
        for transaction in income_transactions:
            income_by_category[transaction.category] += transaction.amount
        
        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'balance': balance,
            'transaction_count': len(self.transactions),
            'income_by_category': dict(income_by_category),
            'expense_by_category': dict(expense_by_category),
            'income_transactions': len(income_transactions),
            'expense_transactions': len(expense_transactions)
        }
    
    def get_monthly_summary(self, year: int, month: int) -> Dict[str, Any]:
        """
        Get summary for a specific month
        
        Args:
            year: Year (e.g., 2024)
            month: Month (1-12)
            
        Returns:
            Dictionary containing monthly summary
        """
        monthly_transactions = [
            t for t in self.transactions 
            if t.date.year == year and t.date.month == month
        ]
        
        income = sum(t.amount for t in monthly_transactions if t.transaction_type == 'income')
        expenses = sum(t.amount for t in monthly_transactions if t.transaction_type == 'expense')
        
        return {
            'year': year,
            'month': month,
            'income': income,
            'expenses': expenses,
            'balance': income - expenses,
            'transaction_count': len(monthly_transactions)
        }
    
    def save_data(self) -> bool:
        """
        Save transactions to JSON file
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            data = {
                'transactions': [t.to_dict() for t in self.transactions],
                'last_updated': datetime.now().isoformat()
            }
            
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self) -> bool:
        """
        Load transactions from JSON file
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not os.path.exists(self.data_file):
                # Create empty file if it doesn't exist
                self.save_data()
                return True
            
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            self.transactions = []
            for transaction_data in data.get('transactions', []):
                transaction = Transaction.from_dict(transaction_data)
                self.transactions.append(transaction)
            
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            self.transactions = []
            return False
    
    def export_to_json(self, filename: str) -> bool:
        """
        Export all data to a specified JSON file
        
        Args:
            filename: Name of the export file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            summary = self.get_summary()
            export_data = {
                'export_date': datetime.now().isoformat(),
                'summary': summary,
                'transactions': [t.to_dict() for t in self.get_all_transactions()]
            }
            
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting data: {e}")
            return False
    
    def clear_all_data(self) -> bool:
        """
        Clear all transactions (use with caution!)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.transactions = []
            self.save_data()
            return True
        except Exception as e:
            print(f"Error clearing data: {e}")
            return False