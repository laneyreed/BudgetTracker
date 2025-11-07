from models.transaction import Transaction
from models.category import Category
from utils.constants import TransactionType


rent = Category(1, "Rent", "Monthly house rent")
groceries = Category(2, "Groceries", "Monthly grocery shopping")
utilities = Category(3, "Utilities", "Monthly utility bills")
transportation = Category(4, "Transportation", "Monthly transport expenses")
entertainment = Category(5, "Entertainment", "Movies, concerts, etc.")
healthcare = Category(6, "Healthcare", "Medical expenses")
other_expense = Category(7, "Other", "Miscellaneous expenses")


trans = Transaction(1, TransactionType.EXPENSE, rent, 1200.0, None, "April rent payment")
print(trans)