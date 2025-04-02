class ExpenseItem:
  def __init__(self):
    self.ask_for_date()
    self.ask_for_category()
    self.ask_for_price()
    self.ask_for_description()

  def ask_for_date(self):
    self.date = "2025-03-05"
    # self.date = input("Enter Date (YYYY-MM-DD): ")

  def ask_for_category(self):
    self.category = "Food"
    # self.category = input("Enter Expense Category: ")

  def ask_for_price(self):
    self.price = 12.12
    # self.price = float(input("Enter Expense Amount: $"))

  def ask_for_description(self):
    self.description = "Lunch with Friends"
    # self.description = input("Enter Description: ")

  def details(self):
    return {"date": self.date, "category": self.category, "amount": self.price, "description": self.description}