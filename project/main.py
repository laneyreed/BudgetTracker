from models.transaction import Transaction
from models.category import Category
from models.user import User
from models.account import Account
from utils.constants import AccountType, TransactionType



user1 = User(id=1, name="Bilbo Baggins", email="bilbo@example.com")
print(f"User Created At: {user1.created_at}")
print(f"User Name: {user1.name}\n"
      f"User ID: {user1.id}"
      f"\nEmail: {user1.email}"
      f"\nPreferred Currency: {user1.currency}"
      )
print("*" * 40)

user1_account1 = Account(name="Chase", account_type=AccountType.CHECKING, user_id=user1, id=1, balance=2500.0)
print(f"Account Created At: {user1_account1.created_at}")
print(f"Account Name: {user1_account1.name}"
      f"\nAccount ID: {user1_account1.id}"
      f"\nAccount Type: {user1_account1.account_type.value}"
      f"\nAccount Owner: {user1_account1.user_id.name}"
      f"\nAccount Owner ID: {user1_account1.user_id.id}"
      f"\nBalance: ${user1_account1.balance:.2f}"
      )
print("*" * 40)


# Category Instances
rent = Category(1, "Rent", "Monthly house rent")
groceries = Category(2, "Groceries", "Monthly grocery shopping")
utilities = Category(3, "Utilities", "Monthly utility bills")
transportation = Category(4, "Transportation", "Monthly transport expenses")
entertainment = Category(5, "Entertainment", "Movies, concerts, etc.")
healthcare = Category(6, "Healthcare", "Medical expenses")
other_expense = Category(7, "Other", "Miscellaneous expenses")


trans = Transaction(1, user1, user1_account1, TransactionType.EXPENSE, rent, 1200.0, None, "April rent payment")
print(f"Transaction Type: {trans.transaction_type.value}" )
print(""f"Transaction ID: {trans.id}"
      f"\nUser Name: {trans.user_id.name}"
      f"\nUser ID: {trans.user_id.id}"
      f"\nAccount: {trans.account_id.name}"
      f"\nCategory: {trans.category.name}"
      f"\nAmount: ${trans.amount:.2f}"
      f"\nDate: {trans.date}"
      f"\nDescription: {trans.description}"
      )
print("*" * 40)