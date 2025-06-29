# Personal Finance Tracker 💰

A command-line personal finance tracker built with Python that helps you manage your income and expenses efficiently.

## Features

- ✅ Add income and expense transactions
- 📊 View financial summaries and reports
- 🏷️ Categorize transactions
- 🔍 Filter transactions by category
- 📤 Export data to JSON
- 💾 Persistent data storage
- 🗑️ Delete transactions
- 💡 Clean, intuitive command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/personal-finance-tracker.git
cd personal-finance-tracker
```

2. Make sure you have Python 3.7+ installed:
```bash
python --version
```

3. Run the application:
```bash
python main.py
```

## Usage

### Starting the Application

Run the main script to start the finance tracker:

```bash
python main.py
```

### Main Menu Options

1. **Add Income** - Record income from various sources (salary, freelance, investments, etc.)
2. **Add Expense** - Record expenses in different categories (food, transport, entertainment, etc.)
3. **View All Transactions** - Display all transactions in chronological order
4. **View Summary** - Show total income, expenses, and balance
5. **View Transactions by Category** - Filter transactions by specific categories
6. **Delete Transaction** - Remove unwanted transactions
7. **Export Data** - Export all data to a JSON file
8. **Exit** - Close the application

### Adding Transactions

**Income Categories:**
- Salary
- Freelance
- Investment
- Other

**Expense Categories:**
- Food
- Transport
- Entertainment
- Utilities
- Shopping
- Healthcare
- Other

### Example Usage

```
--- ADD EXPENSE ---
Enter expense amount: $25.50
Enter description: Lunch at restaurant
Available categories: food, transport, entertainment, utilities, shopping, healthcare, other
Enter category: food
✓ Expense of $25.50 added successfully!
```

## File Structure

```
personal-finance-tracker/
├── main.py              # Main application entry point
├── transaction.py       # Transaction class definition
├── finance_manager.py   # Finance management logic
├── utils.py            # Utility functions
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
└── finance_data.json  # Data storage file (created automatically)
```

## Data Storage

The application stores all data in a JSON file (`finance_data.json`) that is automatically created in the project directory. This file contains:

- All transaction records
- Transaction metadata (ID, timestamp, etc.)
- Last updated timestamp

## Classes and Architecture

### Transaction Class
- Represents individual financial transactions
- Handles data validation and serialization
- Supports both income and expense types

### FinanceManager Class
- Manages all financial operations
- Handles data persistence (save/load)
- Provides summary and filtering capabilities
- Supports data export functionality

### Utility Functions
- Input validation helpers
- Currency formatting
- Screen clearing
- Date formatting

## Features in Detail

### Financial Summary
- Total income and expenses
- Current balance
- Top spending categories
- Transaction counts

### Data Export
- Export to JSON format
- Includes summary statistics
- Timestamped exports
- All transaction details

### Transaction Management
- Unique transaction IDs
- Categories for organization
- Date tracking
- Detailed descriptions

## Development

### Code Style
The project follows Python best practices:
- Type hints for better code documentation
- Docstrings for all classes and methods
- Error handling and validation
- Modular architecture

### Testing
To run tests (if you set up pytest):
```bash
pytest
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Example Screenshots

```
==================================================
           PERSONAL FINANCE TRACKER
==================================================
1. Add Income
2. Add Expense
3. View All Transactions
4. View Summary
5. View Transactions by Category
6. Delete Transaction
7. Export Data
8. Exit
==================================================

--- FINANCIAL SUMMARY ---
Total Income:  $3,500.00
Total Expenses: $2,245.50
Net Balance:   $1,254.50
✓ You're in the green!

Top Expense Categories:
  Food: $450.25
  Transport: $320.00
  Entertainment: $180.75
```

## Future Enhancements

- 📈 Data visualization with charts
- 📅 Monthly/yearly reports
- 🏦 Bank account integration
- 🎯 Budget setting and tracking
- 📱 Mobile app version
- 🔔 Spending alerts
- 📊 Advanced analytics
- 💳 Receipt scanning
- 🌐 Multi-currency support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

**Q: The application won't start**
A: Make sure you have Python 3.7+ installed and all files are in the same directory.

**Q: Data is not saving**
A: Check that you have write permissions in the project directory.

**Q: JSON file is corrupted**
A: Delete the `finance_data.json` file and restart the application to create a fresh data file.

### Error Messages

- **"Invalid input"**: Make sure to enter numbers for amounts and valid categories
- **"File not found"**: The data file will be created automatically on first run
- **"Permission denied"**: Check file permissions in the project directory

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the code comments for implementation details
3. Create an issue on GitHub with details about the problem

## Changelog

### v1.0.0 (Current)
- Initial release
- Basic income/expense tracking
- Category management
- Data export functionality
- Financial summaries
- Transaction deletion

---

**Made with ❤️ in Python**
