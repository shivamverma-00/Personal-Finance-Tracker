"""
Transaction class for the Personal Finance Tracker
"""

import uuid
from datetime import datetime
from typing import Dict, Any

class Transaction:
    """Represents a financial transaction (income or expense)"""
    
    def __init__(self, amount: float, description: str, category: str, 
                 transaction_type: str, date: datetime = None):
        """
        Initialize a new transaction
        
        Args:
            amount: Transaction amount (positive number)
            description: Description of the transaction
            category: Category of the transaction
            transaction_type: 'income' or 'expense'
            date: Transaction date (defaults to current date)
        """
        self.transaction_id = str(uuid.uuid4())
        self.amount = abs(amount)  # Ensure amount is positive
        self.description = description
        self.category = category.lower()
        self.transaction_type = transaction_type.lower()
        self.date = date if date else datetime.now()
        
        # Validate transaction type
        if self.transaction_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary for JSON serialization"""
        return {
            'transaction_id': self.transaction_id,
            'amount': self.amount,
            'description': self.description,
            'category': self.category,
            'transaction_type': self.transaction_type,
            'date': self.date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Transaction':
        """Create transaction from dictionary"""
        transaction = cls(
            amount=data['amount'],
            description=data['description'],
            category=data['category'],
            transaction_type=data['transaction_type'],
            date=datetime.fromisoformat(data['date'])
        )
        transaction.transaction_id = data['transaction_id']
        return transaction
    
    def __str__(self) -> str:
        """String representation of the transaction"""
        return (f"{self.date.strftime('%Y-%m-%d')} - {self.transaction_type.capitalize()}: "
                f"${self.amount:.2f} ({self.category}) - {self.description}")
    
    def __repr__(self) -> str:
        """Developer representation of the transaction"""
        return (f"Transaction(id='{self.transaction_id[:8]}...', "
                f"amount={self.amount}, type='{self.transaction_type}', "
                f"category='{self.category}')")
    
    def __eq__(self, other) -> bool:
        """Compare transactions by ID"""
        if not isinstance(other, Transaction):
            return False
        return self.transaction_id == other.transaction_id
    
    def __hash__(self) -> int:
        """Hash function for transaction"""
        return hash(self.transaction_id)