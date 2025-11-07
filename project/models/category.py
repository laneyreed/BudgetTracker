from utils.constants import DEFAULT_EXPENSE_CATEGORIES, DEFAULT_INCOME_CATEGORIES

class Category:
    def __init__(self, id: int, name: str, description: str = ""):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Category(id={self.id}, name={self.name}, description={self.description})"