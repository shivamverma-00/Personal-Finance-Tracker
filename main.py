#!/usr/bin/env python3
"""
Personal Finance Tracker
A command-line application to track income and expenses
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from transaction import Transaction
from finance_manager import FinanceManager
from utils import clear_screen, get_valid_input, format_currency

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("           PERSONAL FINANCE TRACKER")
    print("="*50)
    print("1. Add Income")
    print("2. Add Expense") 
    print("3. View All Transactions")
    print("4. View Summary")
    print("5. View Transactions by Category")
    print("6. Delete Transaction")
    print("7. Export Data")
    print("8. Exit")
    print("="*50)

def add_income(manager: FinanceManager):
    """Add income transaction"""
    print("\n--- ADD INCOME ---")
    
    amount = get_valid_input("Enter income amount: $", float, lambda x: x > 0, "Amount must be positive")
    description = input("Enter description: ").strip()
    category = input("Enter category (salary/freelance/investment/other): ").strip().lower()
    
    if category not in ['salary', 'freelance', 'investment', 'other']:
        category = 'other'
    
    transaction = Transaction(amount, description, category, 'income')
    manager.add_transaction(transaction)
    print(f"✓ Income of {format_currency(amount)} added successfully!")

def add_expense(manager: FinanceManager):
    """Add expense transaction"""
    print("\n--- ADD EXPENSE ---")
    
    amount = get_valid_input("Enter expense amount: $", float, lambda x: x > 0, "Amount must be positive")
    description = input("Enter description: ").strip()
    
    print("Available categories: food, transport, entertainment, utilities, shopping, healthcare, other")
    category = input("Enter category: ").strip().lower()
    
    if category not in ['food', 'transport', 'entertainment', 'utilities', 'shopping', 'healthcare', 'other']:
        category = 'other'
    
    transaction = Transaction(amount, description, category, 'expense')
    manager.add_transaction(transaction)
    print(f"✓ Expense of {format_currency(amount)} added successfully!")

def view_all_transactions(manager: FinanceManager):
    """Display all transactions"""
    print("\n--- ALL TRANSACTIONS ---")
    transactions = manager.get_all_transactions()
    
    if not transactions:
        print("No transactions found.")
        return
    
    print(f"{'Date':<12} {'Type':<8} {'Category':<12} {'Description':<20} {'Amount':<10}")
    print("-" * 70)
    
    for transaction in transactions:
        print(f"{transaction.date.strftime('%Y-%m-%d'):<12} "
              f"{transaction.transaction_type.capitalize():<8} "
              f"{transaction.category.capitalize():<12} "
              f"{transaction.description[:18]:<20} "
              f"{format_currency(transaction.amount):<10}")

def view_summary(manager: FinanceManager):
    """Display financial summary"""
    print("\n--- FINANCIAL SUMMARY ---")
    summary = manager.get_summary()
    
    print(f"Total Income:  {format_currency(summary['total_income'])}")
    print(f"Total Expenses: {format_currency(summary['total_expenses'])}")
    print(f"Net Balance:   {format_currency(summary['balance'])}")
    
    if summary['balance'] >= 0:
        print("✓ You're in the green!")
    else:
        print("⚠ Warning: Expenses exceed income!")
    
    # Show top spending categories
    if summary['expense_by_category']:
        print("\nTop Expense Categories:")
        for category, amount in sorted(summary['expense_by_category'].items(), 
                                     key=lambda x: x[1], reverse=True)[:3]:
            print(f"  {category.capitalize()}: {format_currency(amount)}")

def view_by_category(manager: FinanceManager):
    """View transactions filtered by category"""
    print("\n--- VIEW BY CATEGORY ---")
    category = input("Enter category to filter by: ").strip().lower()
    
    transactions = manager.get_transactions_by_category(category)
    
    if not transactions:
        print(f"No transactions found for category '{category}'")
        return
    
    print(f"\nTransactions in '{category}' category:")
    print(f"{'Date':<12} {'Type':<8} {'Description':<20} {'Amount':<10}")
    print("-" * 58)
    
    for transaction in transactions:
        print(f"{transaction.date.strftime('%Y-%m-%d'):<12} "
              f"{transaction.transaction_type.capitalize():<8} "
              f"{transaction.description[:18]:<20} "
              f"{format_currency(transaction.amount):<10}")

def delete_transaction(manager: FinanceManager):
    """Delete a transaction by ID"""
    print("\n--- DELETE TRANSACTION ---")
    
    # Show recent transactions with IDs
    transactions = manager.get_all_transactions()[-10:]  # Show last 10
    
    if not transactions:
        print("No transactions to delete.")
        return
    
    print("Recent transactions:")
    for i, transaction in enumerate(transactions):
        print(f"{i+1}. {transaction.date.strftime('%Y-%m-%d')} - "
              f"{transaction.description} - {format_currency(transaction.amount)}")
    
    try:
        choice = int(input(f"\nEnter transaction number to delete (1-{len(transactions)}): "))
        if 1 <= choice <= len(transactions):
            transaction_to_delete = transactions[choice-1]
            if manager.delete_transaction(transaction_to_delete.transaction_id):
                print("✓ Transaction deleted successfully!")
            else:
                print("✗ Failed to delete transaction.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def export_data(manager: FinanceManager):
    """Export data to JSON file"""
    print("\n--- EXPORT DATA ---")
    filename = input("Enter filename (without extension): ").strip()
    if not filename:
        filename = f"finance_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    filename += ".json"
    
    if manager.export_to_json(filename):
        print(f"✓ Data exported successfully to {filename}")
    else:
        print("✗ Failed to export data.")

def main():
    """Main application loop"""
    # Initialize finance manager
    manager = FinanceManager()
    
    print("Welcome to Personal Finance Tracker!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                add_income(manager)
            elif choice == '2':
                add_expense(manager)
            elif choice == '3':
                view_all_transactions(manager)
            elif choice == '4':
                view_summary(manager)
            elif choice == '5':
                view_by_category(manager)
            elif choice == '6':
                delete_transaction(manager)
            elif choice == '7':
                export_data(manager)
            elif choice == '8':
                print("Thank you for using Personal Finance Tracker!")
                break
            else:
                print("Invalid choice. Please select 1-8.")
            
            input("\nPress Enter to continue...")
            clear_screen()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()