from datetime import datetime
from models.category import Category
from utils.constants import TransactionType


class Transaction:
    def __init__(self, id: int, transaction_type: TransactionType, category: Category, amount: float, date: datetime, description: str):
        self.id = id
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.date = date or datetime.now()
        self.description = description
        


    def __str__(self):
        return f"Transaction(id={self.id}, category={self.category}, amount={self.amount}, date={self.date}, description={self.description}, transaction_type={self.transaction_type})"
