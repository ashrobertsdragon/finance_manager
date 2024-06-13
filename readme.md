# Personal Finance Manager

A simple personal finance tracking app designed to manage accounts, transactions, and categories effectively.

## Project Overview

This project, **pf_manager**, is a Python-based application that helps you track and manage your personal finances. The app includes features for handling multiple accounts, categorizing transactions, and performing fund transfers between accounts.

## Features

- Account Management: Create and manage multiple accounts including Debit, Credit, and Equity accounts.

- Transaction Management: Add, remove, and categorize transactions.

- Category Management: Define and manage categories to organize transactions.

- Fund Transfer: Transfer funds between accounts with automated transaction logging.

## Installation

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Usage

### Account Management

Create an account and manage your balance:

```python
from datetime import datetime
from pf_manager import DebitAccount, CreditAccount, EquityAccount, AccountManager

# Create accounts
debit_account = DebitAccount(account_name="Checking Account", account_number="123456789", balance=100000)  # balance in cents
credit_account = CreditAccount(account_name="Credit Card", account_number="987654321", balance=-50000)

# Manage accounts
account_manager = AccountManager()
account_manager.add_account(debit_account)
account_manager.add_account(credit_account)
```

### Transaction Management

Add transactions to your accounts:

```python
from pf_manager import Transaction, TransactionManager, Category

# Create categories
grocery_category = Category(name="Grocery")
entertainment_category = Category(name="Entertainment")

# Create transactions
transaction1 = Transaction(date=datetime.now(), amount=5000, description="Grocery Shopping", category=grocery_category)
transaction2 = Transaction(date=datetime.now(), amount=2000, description="Movie Ticket", category=entertainment_category)

# Manage transactions
transaction_manager = TransactionManager(transactions=[transaction1])
transaction_manager.add_transaction(transaction2)
```

### Fund Transfer

Transfer funds between accounts:

```python
# Transfer funds
amount_to_transfer = 3000  # amount in cents
account_manager.transfer_funds(debit_account, credit_account, amount_to_transfer)
```

## Project Structure

- Category: Represents a category for transactions.
- Transaction: Represents a financial transaction.
- CategoryManager: Manages categories.
- TransactionManager: Manages transactions.
- Account: Base class for different types of accounts.
- DebitAccount, CreditAccount, EquityAccount: Specific account types.
- AccountManager: Manages multiple accounts and performs fund transfers.
- Bank: Represents a bank containing multiple accounts.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
