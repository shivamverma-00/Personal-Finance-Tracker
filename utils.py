"""
Utility functions for the Personal Finance Tracker
"""

import os
import sys
from typing import Any, Callable, TypeVar

T = TypeVar('T')

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_currency(amount: float) -> str:
    """
    Format a number as currency
    
    Args:
        amount: The amount to format
        
    Returns:
        Formatted currency string
    """
    return f"${amount:,.2f}"

def get_valid_input(prompt: str, input_type: type = str, 
                   validator: Callable[[Any], bool] = None,
                   error_message: str = "Invalid input") -> Any:
    """
    Get valid input from user with type checking and validation
    
    Args:
        prompt: The input prompt to display
        input_type: Expected type of input (int, float, str)
        validator: Optional validation function
        error_message: Error message to display for invalid input
        
    Returns:
        Validated input of the specified type
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Convert to the specified type
            if input_type == str:
                converted_input = user_input
            elif input_type == int:
                converted_input = int(user_input)
            elif input_type == float:
                converted_input = float(user_input)
            else:
                converted_input = input_type(user_input)
            
            # Apply validator if provided
            if validator and not validator(converted_input):
                print(f"Error: {error_message}")
                continue
            
            return converted_input
            
        except ValueError:
            print(f"Error: Please enter a valid {input_type.__name__}")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(0)

def get_yes_no_input(prompt: str, default: bool = None) -> bool:
    """
    Get yes/no input from user
    
    Args:
        prompt: The prompt to display
        default: Default value if user just presses Enter
        
    Returns:
        True for yes, False for no
    """
    while True:
        try:
            if default is not None:
                default_text = " (Y/n)" if default else " (y/N)"
                response = input(prompt + default_text + ": ").strip().lower()
                
                if not response:
                    return default
            else:
                response = input(prompt + " (y/n): ").strip().lower()
            
            if response in ['y', 'yes', '1', 'true']:
                return True
            elif response in ['n', 'no', '0', 'false']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return False

def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length
    
    Args:
        text: The string to truncate
        max_length: Maximum length of the string
        suffix: Suffix to add when truncating
        
    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def validate_positive_number(value: float) -> bool:
    """Validate that a number is positive"""
    return value > 0

def validate_non_empty_string(value: str) -> bool:
    """Validate that a string is not empty"""
    return len(value.strip()) > 0

def format_date(date_obj) -> str:
    """
    Format a datetime object as a readable string
    
    Args:
        date_obj: datetime object
        
    Returns:
        Formatted date string
    """
    return date_obj.strftime("%Y-%m-%d %H:%M")

def print_separator(char: str = "-", length: int = 50):
    """Print a separator line"""
    print(char * length)

def print_header(title: str, char: str = "=", length: int = 50):
    """Print a formatted header"""
    print(char * length)
    print(f"{title:^{length}}")
    print(char * length)

def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """
    Safely divide two numbers, returning default if division by zero
    
    Args:
        numerator: The numerator
        denominator: The denominator
        default: Default value to return if denominator is zero
        
    Returns:
        Result of division or default value
    """
    try:
        return numerator / denominator if denominator != 0 else default
    except (TypeError, ZeroDivisionError):
        return default

def get_file_size(filepath: str) -> str:
    """
    Get human-readable file size
    
    Args:
        filepath: Path to the file
        
    Returns:
        Human-readable file size string
    """
    try:
        size = os.path.getsize(filepath)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
    except OSError:
        return "Unknown"

def create_backup_filename(original_filename: str) -> str:
    """
    Create a backup filename with timestamp
    
    Args:
        original_filename: Original filename
        
    Returns:
        Backup filename with timestamp
    """
    from datetime import datetime
    
    name, ext = os.path.splitext(original_filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{name}_backup_{timestamp}{ext}"