from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


@dataclass
class Category:
    name: str
    parent_category: Optional['Category'] = None


@dataclass
class Transaction:
    date: datetime
    amount: int  # Store amount in cents
    description: str
    category: Category


class CategoryManager:
    def __init(self, categories: List[Category]):
        self.categories = categories

    def add_category(self, cat: Category) -> None:
        self.categories.append(cat)

    def remove_category(self, cat: Category) -> None:
        self.categories.remove(cat)

    def filter_category(self, filter_func) -> List[Category]:
        return list(filter_func(self.categories))


class TransactionManager:
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, transaction: Transaction):
        self.transactions.remove(transaction)

    def categorize_transaction(
        self, transaction: Transaction, category: Category
    ):
        transaction.category = category

    def filter_transactions(self, filter_func):
        return list(filter(filter_func, self.transactions))


class Account(BaseModel):
    account_name: str
    account_number: str
    balance: int  # Store balance in cents
    transaction_manager: TransactionManager = Field(
        default_factory=TransactionManager
    )

    def check_balance(self, amount: int) -> bool:
        raise NotImplementedError

    def apply_transaction(self, amount: int):
        raise NotImplementedError


class DebitAccount(Account):
    pass


class CreditAccount(Account):
    pass


class EquityAccount(Account):
    pass


class AccountManager(BaseModel):
    accounts: List[Account] = Field(default_factory=list)

    def add_account(self, account: Account):
        self.accounts.append(account)

    def remove_account(self, account: Account):
        self.accounts.remove(account)

    def transfer_funds(
        self, from_account: Account, to_account: Account, amount: int
    ):
        from_account.apply_transaction(-amount)
        to_account.apply_transaction(amount)

        transaction_out = Transaction(
            date=datetime.now(),
            amount=-amount,
            description="Transfer Out",
            category=Category(name="Transfer")
        )
        transaction_in = Transaction(
            date=datetime.now(),
            amount=amount,
            description="Transfer In",
            category=Category(name="Transfer")
        )
        from_account.transaction_manager.add_transaction(transaction_out)
        to_account.transaction_manager.add_transaction(transaction_in)


class Bank(BaseModel):
    name: str
    accounts: List[Account] = Field(default_factory=list)

    def add_account(self, account: Account):
        self.accounts.append(account)
